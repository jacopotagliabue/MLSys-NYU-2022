# Homework 1

For each problem, you should submit a python file (a "script") with the question name, like `question_1.py`, `question_2.py`, etc... These files should only use standard python or the libraries that are included in `requirements.txt`. Your grader should be able to install the libraries from `requirements.txt` into a virtual environment and then run your script from the command line like:

```commandline
python question_1.py
```

You can assume that your grader is running the script from the same folder that this document is in.

## 1. Linear Regression by Hand


Recall the linear regression model from class:

$$\hat{y}_{i} = \beta_{0} + \sum_{j=1}^{p}x_{ij}\beta_{j}$$

where $\hat{y}_{i}$ is the prediction for the ith sample, $x_{ij}$ is the jth feature for the ith sample, $\beta_{j}$ is the jth _coefficient_ or _parameter_ of our linear model, and $\beta_{0}$ is the bias or intercept term. We showed how we can turn this into a matrix equation:

$$\hat{\vec{y}} = \mathbf{X}\vec{\beta}$$

where we've assumed that $X_{i0} = 1$ in order to handle the bias term. Lastly, we showed how to minimize the mean squared error between this model's predictions and the true values $\vec{y}$ in order to analytically solve for the optimal values of $\vec{\beta}$:

$$
\vec{\beta} = \left(\mathbf{X}^{\intercal}\mathbf{X}\right)^{-1}\mathbf{X}^{\intercal}\vec{y} \tag{1}
$$

In this homework problem, you will learn how to use `numpy` to fit a linear regression model. Please write a script that:

1. Reads in the housing data `train.csv` dataset to a Pandas DataFrame.
2. Creates an $\mathbf{X}$ matrix as a numpy array. For this $\mathbf{X}$ matrix, use the columns (aka features) `1stFlrSF`, `2ndFlrSF`, and `TotalBsmntSF`. In the `scientific_computing.ipynb` notebook, we combined all these columns into a single feature. For this task, we will leave them as separate features and see if that improves the model prediction.
3. Creates a $\vec{y}$ vector as a `numpy` array out of the `SalePrice` column.
4. Creates a $\vec{\beta}$ vector as a `numpy` array using Equation (1).
5. Generates predictions $\hat{y}$ using your $\vec{\beta}$ vector.
6. Calculates and prints out the $\mathcal{R}^{2}$ value between your predictions and the true values.

Notes:
- Do not use `scikit-learn` for this. You should only use `pandas` and `numpy`.
- See the documentation for `np.concatenate` for information on how to stack together arrays.
- You cannot use `array**-1` to take the inverse of a numpy array. You must use `np.linalg.inv(array)`.

## 2. More Features 

In the `scientific_computing.ipynb` notebook, we saw how to fit a single feature linear regressin model using `scikit-learn`. In this question, you will fit a similar linear regression model using varying numbers of features, and you will observe how the model's performance changes with the number of features.

Please write a script that:

1. Reads in the housing data `train.csv` dataset.
2. Using this list of features
    ```python
    [
        "1stFlrSF",
        "2ndFlrSF",
        "TotalBsmtSF",
        "LotArea",
        "OverallQual",
        "GrLivArea",
        "GarageCars",
        "GarageArea",
    ]
    ```
    fit a linear regression model with `scikit-learn` using just the first feature, fit a model using the first 2 features, fit a model using the first 3 features, etc... In the end, you should fit 9 separate models. Please use a `for` loop for this rather than manually writing the code 8 times.
3. For each model, use `scikit-learn` to calculate the $R^{2}$, Mean Squared Error, Mean Absolute Error, and Mean Absolute Percentage Error.
4. Finally, generate a plot for each performance metric. The x-axis should be the number of features in the model, and the y-axis is the value of the metric.

Notes:
- When running a script, use `matplotlib.pyplot.show()` to open a window showing the plot. The script will pause execution while you view the plot. If you close the plot, then the script will continue again.
- Try to use loops and/or functions so that you are not copying and pasting code many times.
