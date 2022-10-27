"""
Simple playground from https://www.comet.ml/docs/python-sdk/scikit/, to make sure the COMET
account is working and the initialization logic is understood.
We initialize COMET using the ENV VARIABLE option, as explained here:
https://www.comet.ml/docs/python-sdk/advanced/#python-configuration
You are also required to specify a project name for this sample project, e.g. jt3341nyu_comet_test.
To avoid duplications, always use your NYU ID first in the project name!

From the command line you can cd into this folder and run
COMET_API_KEY=xxx MY_PROJECT_NAME=yyy python comet_playground.py

At the end, log in into the dashboard and check all looks good!
If you prefer alternative init methods, feel free to change the code to whatever method 
you prefer, and use this script to validate your COMET setup.
"""

import os
# MAKE SURE THESE VARIABLES HAVE BEEN SET
assert 'COMET_API_KEY' in os.environ and os.environ['COMET_API_KEY']
assert 'MY_PROJECT_NAME' in os.environ and os.environ['MY_PROJECT_NAME']
print("Running experiment for project: {}".format(os.environ['MY_PROJECT_NAME']))

from comet_ml import Experiment
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix


def main():
    #create an experiment with your api key
    exp = Experiment(project_name=os.environ['MY_PROJECT_NAME'],
                    auto_param_logging=False)
    random_state = 42

    cancer = load_breast_cancer()
    print("cancer.keys(): {}".format(cancer.keys()))
    print("Shape of cancer data: {}\n".format(cancer.data.shape))
    print("Sample counts per class:\n{}".format(
        {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
    print("\nFeature names:\n{}".format(cancer.feature_names))

    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data,
        cancer.target,
        stratify=cancer.target,
        random_state=random_state)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    logreg = LogisticRegression()

    param_grid = {'C':[0.001,0.01,0.1,1,5,10,20,50,100]}

    clf = GridSearchCV(logreg,
                        param_grid=param_grid,
                        cv=10,
                        n_jobs=-1)

    clf.fit(X_train_scaled, y_train)

    y_pred = clf.predict(X_test_scaled)

    print("\nResults\nConfusion matrix \n {}".format(confusion_matrix(y_test, y_pred)))

    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print("F1 score is {:6.3f}".format(f1))
    print("Precision score is {:6.3f}".format(precision))
    print("Recall score is {:6.3f}".format(recall))

    #these will be logged to your sklearn-demos project on Comet.ml
    params={"random_state":random_state,
            "model_type":"logreg",
            "scaler":"standard scaler",
            "param_grid":str(param_grid),
            "stratify":True
    }

    metrics = {"f1":f1,
    "recall":recall,
    "precision":precision
    }

    exp.log_dataset_hash(X_train_scaled)
    exp.log_parameters(params)
    exp.log_metrics(metrics)

    return


if __name__ == "__main__":
    main()