"""

Slightly revised version of:

https://github.com/jacopotagliabue/reclist/blob/7e28d630892e5fa42be1a417af020a15a723a591/reclist/recommenders/prod2vec.py#L56

Check the RecList (https://reclist.io/) project for background on the abstractions.

"""


import numpy as np
from reclist.abstractions import RecModel
from reclist.utils.train_w2v import train_embeddings


class SpotifyModel(RecModel):
    """
    Implement of the prod2vec model through the standard RecModel interface.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    model_name = "prod2vec"

    def train(self, playlists, window=5):
        # TODO: pass kwargs to the training method, so that we can parametrize
        # the entire training
        x_train_uris = [[track['track_uri'] for track in playlist] for playlist in playlists]
        self._model = train_embeddings(
            x_train_uris, 
            min_c=2,
            size=48,
            window=window,
            iterations=15,
            ns_exponent=0.75
            )

    def predict(self, prediction_input: list, *args, **kwargs):
        """
        NEP following industry best practices mentioned in https://arxiv.org/abs/2007.14906:
        given a trained prod2vec, take all the seeded (or before-last) tracks to construct a
        playlist vector by average pooling, and use kNN to predict the next items (or the last
        item).
        """
        predictions = []
        for _x in prediction_input:
            embeddings = [self._model[track['track_uri']] for track in _x if track['track_uri'] in self._model]
            if embeddings:
                avg_playlist_vector = np.average(embeddings, axis=0)
                nn_tracks = self._model.similar_by_vector(avg_playlist_vector, topn=100)
                predictions.append([{'track_uri':_[0]} for _ in nn_tracks])
            else:
                predictions.append([])

        return predictions

    def get_vector(self, track_uri):
        try:
            return list(self._model.get_vector(track_uri))
        except Exception as e:
            return []