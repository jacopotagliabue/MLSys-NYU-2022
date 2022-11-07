# Homework #5 (due 11/18/2022)

## Task 1: implement a fairness test (50%)

First, generate some synthetic data for a classification task (e.g. approving loans), and make sure to have as input feature (among others, zip code, age etc.) a categorical variable such as gender or race (fill it with proper random values). You will be using this dataset to implement two sets of tests:

* test 1: measure the generalization of the model over the entire test set with your favorite classification metric (e.g. accuracy, f1 etc.);
* test 2: operationalize (as a first attempt) the concept of "fairness" among groups that we discussed in class. In particular, implement the test based on Miss Rate explained [here](https://arxiv.org/pdf/2207.05772.pdf) - Section 3.3.2. Your job is to understand the definition and implement it correctly to check how your model is doing (question: if your dataset is truly random, what should we expect?).

Your deliverable is a full-fledged Metaflow pipeline, containing the dataset as input, training a model of your choice, and then doing standard and per-group tests.

## Task 2: a streamlit app for interactive analysis (25%)

Building on Task 1, add a Streamlit application that will:

* load the latest model and the latest dataset from your Flow;
* show a drop-down menu that lets users explore the performance of the model on a given subgroup: changing the value in the menu should display a new chart (or paragraph) (remember: put yourself in the shoes of a user that did not train the model - what should we tell her to explain what the model does?).

## Task 3: producing custom cards (25%)

You can easily customize DAG [cards](https://docs.metaflow.org/metaflow/visualizing-results/easy-custom-reports-with-card-components) to improve the documentation that gets automatically generated for you.

Building on top of your Flow for Task 1, add a custom card on the testing _step_ in your pipeline: in the card, produce a bar chart that displays the Miss Rate for each of the target sub-groups, so that it is easy to visually check which group is doing better or worse. 

Make sure then when you run the flow *--with card*, the card is then visible and is displaying the chart properly.