"""

Simple stand-alone script showing end-to-end training of a regression model. This script mimics
an implementation in which we break down the monolith script into logical steps. This script
has been created for pedagogical purposes, and it does NOT reflect best practices.

Please refer to the slides and our discussion for further context.

"""


import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model, metrics
from collections import namedtuple
from datetime import datetime


# namedtuple to contain the dataset and splits
Dataset = namedtuple('Dataset', 'Xs Ys')
Splits = namedtuple('Splits', 'X_train, X_test, y_train, y_test')
Regression = namedtuple('Regression', 'model beta intercept')
RegressionMetrics = namedtuple('RegressionMetrics', 'mse r2')


def load_data(file_name: str, is_debug=False) -> Dataset: 
    """
    Load data from csv file
    """
    Xs = []
    Ys = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            x, y = line.split('\t')
            Xs.append([float(x)])
            Ys.append(float(y))

    if is_debug:
        print(len(Xs), len(Ys))

    return Dataset(Xs, Ys)


def check_dataset(data: Dataset) -> bool:
    """
    Mimic a quality check on the data, for example checking the Ys are within a certain range.
    There are good packages to do this in a more structured way (https://greatexpectations.io/).

    We will discuss in class some of the tools of a modern data pipeline, e.g 
    (https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat)
    """
    assert(all(y < 100 and y > -100 for y in data.Ys))

    return True


def prepare_train_and_test_dataset(data: Dataset, test_size: float=0.20, seed: int=42) -> Splits:
    """
    Split data into train and test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        data.Xs, 
        data.Ys, 
        test_size=test_size, 
        random_state=seed
        )

    return Splits(X_train, X_test, y_train, y_test)


def train_model(splits: Splits, is_debug: bool=True) -> Regression:
    """
    Train a linear regression model and return the scikit object, coeff and intercept
    """
    reg = linear_model.LinearRegression()
    reg.fit(splits.X_train, splits.y_train)
    if is_debug:
        print("Coefficient {}, intercept {}".format(reg.coef_[0], reg.intercept_))

    return Regression(reg, reg.coef_[0], reg.intercept_)


def plot_points(y_predicted: list, y_test: list, plot_name: str) -> None:
    """
    Plot actual vs predicted and save the figure to disk
    """
    fig, ax = plt.subplots()
    ax.scatter(y_predicted, y_test, edgecolors=(0, 0, 1))
    ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', lw=3)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    plt.savefig(plot_name, bbox_inches='tight')

    return


def evaluate_model(model: linear_model, splits: Splits,  with_plot: bool=True, is_debug: bool=True) -> RegressionMetrics:
    """
    Predict unseeen values and evaluate the model with standard regression metrics
    """
    y_predicted = model.predict(splits.X_test)
    mse = metrics.mean_squared_error(splits.y_test, y_predicted)
    r2 = metrics.r2_score(splits.y_test, y_predicted)

    if is_debug:
        print('MSE is {}, R2 score is {}'.format(mse, r2))

    if with_plot:
        plot_points(y_predicted, splits.y_test, 'composable_regression_analysis.png')

    return RegressionMetrics(mse, r2)


def composable_script(file_name: str, test_size: float=0.20):
    # starting up!
    print("Starting up at {}".format(datetime.utcnow()))
    # read the data into a tuple
    dataset = load_data(file_name)
    # check data quality
    is_data_valid = check_dataset(dataset)
    # split the data 
    splits = prepare_train_and_test_dataset(dataset, test_size=test_size)
    # train the model
    regression = train_model(splits, is_debug=True)
    # evaluate model
    model_metrics = evaluate_model(regression.model, splits, with_plot=True)
    # all done
    print("All done at {}!\n See you, space cowboys!".format(datetime.utcnow()))

    return


if __name__ == "__main__":
    # TODO: we can move this to read from a command line option, for example
    FILE_NAME = 'regression_dataset.txt'
    TEST_SIZE = 0.20
    composable_script(FILE_NAME, TEST_SIZE)