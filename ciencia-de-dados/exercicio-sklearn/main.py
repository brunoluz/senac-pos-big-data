import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
from matplotlib import pyplot

from pandas import read_excel
from pandas.plotting import scatter_matrix


def execute():
    dataset = read_excel("renda_anual.xlsx")

    print(f"dataset shape (rows, columns): {dataset.shape}")

    print("dataset head:")
    print(dataset.head())

    print("dataset describe:")
    print(dataset.describe())

    print("dataset info:")
    print(dataset.info())

    # class distribution
    print("dataset class distribution:")
    print(dataset.groupby('faixa de renda anual').size())

    # box and whisker plots
    dataset.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
    pyplot.show()

    # histograms
    dataset.hist()
    pyplot.show()

    # scatter plot matrix
    scatter_matrix(dataset)
    pyplot.show()


if __name__ == '__main__':
    execute()
