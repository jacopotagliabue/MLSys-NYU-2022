"""

Simple stand-alone script to create a txt file representing a fake datasets 
to train a regression model later on.

"""

from sklearn import datasets
import matplotlib.pyplot as plt


def plot_scatter(x: list, y: list):
    plt.title('X Vs. Y')
    plt.plot(x, y, '.', label='dataset')
    plt.savefig('regression.png', bbox_inches='tight')

    return


def main():
    x, y, coef = datasets.make_regression(
        n_samples=1000, # number of samples
        n_features=1, # number of features
        n_informative=1, # number of useful features 
        noise=10, # guassian noise
        coef=True,
        random_state=42)
    # dump data to a local txt file
    with open('regression_dataset.txt', 'w') as f:
        for _x, _y in zip(x, y):
            f.write('{}\t{}\n'.format(_x[0], _y))
    # print the coefficient and plot it for visual inspection
    print("Generated sample data, coefficient: {}".format(coef))
    plot_scatter(x, y)

    return


if __name__ == "__main__":
    main()