# Week 13

## Building a recommender system

We will use a subset of the [The Million Playlist Dataset](https://engineering.atspotify.com/2018/05/introducing-the-million-playlist-dataset-and-recsys-challenge-2018/) to implement a simple sequential recommender, building on top of the intuitions we developed last time wrt embeddings and similarity:

* the `src` folder contains a Metaflow flow training a Song2Vec recommender and storing embeddings as artifacts with the usual syntax. The code makes essential use of the convenient abstractions from the [RecList](https://reclist.io/) library, to avoid a lot of boilerplate when getting the Spotify dataset and train the Song2Vec model (note that we also get advanced testing for free!). As usual, `requirements.txt` contains the necessary dependencies to run the flow;
* the `notebooks` folder contains exploratory code - _after_ you run the pipeline, you can use the notebook to explore the artifacts, and in particular the embedding space and predictions made by the recommender system we trained.

## Misc. Links

* Our introduction to RecSys has been unorthodox in many ways: embeddings are usually part of a deep learning course, and are considered advanced systems. However, for reasons explained in class, we believe there is value in seeing RecSys through the lenses of similarity judgements, and treat embeddings as machine-friendly way to encode that similarity. For more classific algorithms and ideas, check [SVD](https://pantelis.github.io/cs301/docs/common/lectures/recommenders/netflix/) as the standard matrix factorization algorithm, or the very practical [Apriori algo](https://deepak6446.medium.com/apriori-algorithm-in-python-recommendation-engine-5ba89bd1a6da), which does not even use machine learning.
* For a Kaggle-based walkthrough into RecSys, [this](https://www.kaggle.com/competitions/otto-recommender-system/discussion/368560) by Radek Osmulski (NVIDIA) is a great place to start. 
* If you are enjoying Metaflow, [this](https://github.com/jacopotagliabue/recs-at-resonable-scale) is a fully open source project combining Metaflow and Two-Tower models (deep learning) for a fashion use case (shopper-item).
* Your professor published extensively on RecSys, including [sequential recs](https://aclanthology.org/2021.ecnlp-1.1/), [model evaluation](https://jacopotagliabue.it/public/Wild_Wild_Tests_MLOPS_World_2022.pdf), open source [testing](https://reclist.io/), [MLOps](https://www.youtube.com/watch?v=9rouLchcC0k&t=147s).