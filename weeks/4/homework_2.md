# Homework 2

For each problem, you should submit a python file (a "script") with the question name, like `question_1.py`, `question_2.py`, etc... These files should only use standard python or the libraries that are included in `requirements.txt`. Your grader should be able to install the libraries from `requirements.txt` into a virtual environment and then run your script from the command line like:

```commandline
python question_1.py
```

You can assume that your grader is running the script from the same folder that this document is in.

#### Also

While you are free to write your code however you want, you are expected to clean up the code prior to submitting it for grading. Primarily, this means remove commented code or unnecessary comments from your code. For example, if you write the code in a Jupyter notebook and export it to a script, then you should remove the comments indicating the cell numbers.

Machine learning is a team sport, and good team members make it easy for their teammates to read their code.

## 1. Multiclass Text Classifcation (30%)

For this problem, you will learn how to classify text documents. 

In your script, use scikit-learn's [fetch_20newsgroups()](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html) function to download both the training and test newsgroups datasets. Each sample in these datasets is a written message, and each message belongs to a specific _newsgroup_. See [here](http://qwone.com/~jason/20Newsgroups/) for more info about the dataset.

The goal of this question is to predict which newsgroup a message belongs to (i.e. the newsgroup is the class in a multiclass classification problem).

You cannot pass the text directly into a machine learning model, so use the [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to extract features out of the text. You should read about this vectorizer so that you know what you're doing!

For this problem, your script should

1. Download the training and test data.
2. Generate TF-IDF features.
3. Train a Logistic Regression model off of said features.
4. Calculate a multiclass classification report on the test data.

Finally, in commented code at the bottom of the script, write about which newsgroups your model has the highest and lowest precision on and explain why you think the model performs the way that it does on these newsgroups.

## 2. Pipeline Gridsearch (70%)

For this problem, you will carry out a full model selection via cross validation using a scikit-learn [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).

Similar to this week's [notebook](notebooks/classification.ipynb), you will use the Airline Passenger Satisfaction data that is located at [data/airline_satisfaction/train.csv](data/airline_satisfaction/train.csv) to predict whether or not the customer was satisfied. 

To start, construct a single `Pipeline` that:

1. Scales all numerical features (except for the `id` column).
2. One-hot-encodes all categorical features.
3. Handles missing data.
4. Fits a `LogisticRegression` model.

You might find the [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html) helpful.

Split your data into `training` and `test` data. Then, using [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), conduct a grid search that:

1. Uses the `pipeline` that you've built as the estimator.
2. Uses 5-fold cross validation.
3. Searches across at least 2 different values for 3 different hyperparameters.
4. Maximizes the Area Under the ROC Curve.

Finally, given the optimal hyperparameters that you've found, train a model on the full training dataset and then print out the Area Under the ROC Curve for the test set of data.
