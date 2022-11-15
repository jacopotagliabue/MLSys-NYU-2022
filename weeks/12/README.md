# Week 12

## Representation learning: an introduction through NLP

In the lecture, we explained the importance of "similarity" for recommender systems, and how vector representations can be a good proxy in a "proper" latent space.

We build our intuition on embeddings starting from the well-understood case of word embeddings in NLP ("word2vec"); in particular, we learn that by specifying a suitable prediction task, the learning dynamics will naturally push "closer in the space" embeddings of similar items.

The `notebooks` folder contains some sample code to train word2vec from scratch on a corpus, and some data viz to understand what the space actually encodes after training (needed packages are indicated directly in-line in the cells).

## Misc. Links

* A fantastic introduction to word embeddings by [Piero Molino](https://w4nderlu.st/media/pages/teaching/word-embeddings/2739226721-1665242033/word-embeddings.pdf).
* Last year's [slides on NLP](https://github.com/jacopotagliabue/FREE_7773).
* [Glove](https://nlp.stanford.edu/projects/glove/), a popular alternative to skip-gram / Word2Vec for word embeddings.
* Skip-gram embeddings are produced by shallow neural networks, but of course the concepts of embeddings and representations is a crucial component of modern deep learning. A good, practical introduction is the [Keras book](https://www.amazon.com/Learning-Python-Second-Fran-C3-A7ois-Chollet-dp-1617296864/dp/1617296864/ref=dp_ob_title_bk).