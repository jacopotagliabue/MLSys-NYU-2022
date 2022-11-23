"""

A Metaflow pipeline showing how to use skip-gram based embeddings for music songs 
to recommend new tracks to users.

Original dataset wrapper and testing code coming from RecList:

https://github.com/jacopotagliabue/reclist/blob/main/examples/spotify_session_rec.py

Please check the README in this repository for background info.

"""


from metaflow import FlowSpec, step, current


class PlaylistRecsFlow(FlowSpec):

    @step
    def start(self):
        """
        Start-up: check everything works!
        """
        # debug printing
        print("flow name: %s" % current.flow_name)
        print("run id: %s" % current.run_id)
        print("username: %s" % current.username)
        # next up, get the data
        self.next(self.prepare_dataset)

    @step
    def prepare_dataset(self):
        """
        Get the Spotify dataset in a convenient shape by using the
        abstractions provided by RecList (https://reclist.io/)

        NOTE: THIS MAY TAKE A WHILE THE FIRST TIME AS THE DATASET GETS DOWNLOADED!
        """
        from reclist.datasets import SpotifyDataset
        # get the Spotify million playlist dataset as a RecDataset object
        self.spotify_dataset = SpotifyDataset(force_download=False)
        # check the dataset by printing out the first playlist
        print("First playlist is", self.spotify_dataset.x_train[0][0]['playlist_name'])
        self.data_catalog = self.spotify_dataset.catalog
        test_track = self.data_catalog[list(self.data_catalog.keys())[0]]
        print("First track metadata is", test_track['track_name'], test_track['artist_name'], test_track['album_name'])
        # next up, generate vectors for songs from existing playlists
        # hypers are just window lenghts as an example
        self.hypers_sets = [5] # [3, 10]
        self.next(self.generate_embeddings, foreach='hypers_sets')

    @step
    def generate_embeddings(self):
        """
        Generate vector representations for songs, based on Word2Vec.

        For an overview of the algorithm and the evaluation, see for example:
        https://arxiv.org/abs/2007.14906
        """
        from spotifyModel import SpotifyModel
        from reclist.reclist import SpotifySessionRecList
        # get the current value of the hyper in the foreach
        self.window_length = int(self.input)
        # instantiate and train the skip-gram model
        model = SpotifyModel()
        model.train(self.spotify_dataset.x_train)
        print("Training with window {} is completed!".format(self.window_length))
        # finally, version the embeddings as key values
        self.track_vectors = model._model
        rec_list = SpotifySessionRecList(
            model=model,
            dataset=self.spotify_dataset
        )
        rec_list(verbose=True)
        self.rec_list_results = rec_list.test_results
        # display the HR@10 test result
        self.hit_rate = next(res for res in self.rec_list_results if res['test_name'] == 'HR@10')['test_result']
        # join with the other runs
        self.next(self.join_runs)

    @step
    def join_runs(self, inputs):
        """
        Join the parallel runs and merge results into a dictionary.
        """
        # merge results from runs with different window params
        self.all_vectors = { inp.window_length: inp.track_vectors for inp in inputs}
        self.all_results = { inp.window_length: inp.hit_rate for inp in inputs}
        print("Current result map: {}".format(self.all_results))
        self.best_model, self_best_result = sorted(self.all_results.items(), key=lambda x: x[1], reverse=True)[0]
        print("The best score is for model: {}, {}".format(self.best_model, self_best_result))
        # assign as "final" the best vectors for downstream tasks
        self.final_vectors = self.all_vectors[self.best_model]
        self.final_dataset = inputs[0].spotify_dataset.x_train
        self.final_catalog = inputs[0].data_catalog
        # all done, say goodbye!
        self.next(self.end)

    @step
    def end(self):
        """
        Just say bye!
        """
        print("All done\n\nSee you, space cowboy\n")
        return


if __name__ == '__main__':
    PlaylistRecsFlow()