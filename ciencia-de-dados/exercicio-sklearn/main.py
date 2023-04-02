import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
from matplotlib import pyplot

from pandas import read_excel
from pandas.plotting import scatter_matrix


def column_to_number(df, original_column_name, numerical_column_name):
    category = df[original_column_name].astype('category')
    df[numerical_column_name] = category.cat.codes
    return dict(enumerate(category.cat.categories))


def execute():
    df = read_excel("renda_anual_02.xlsx")

    tipo_emprego_codes = column_to_number(df, 'tipo_emprego', 'tipo_emprego_cod')
    estado_civil_codes = column_to_number(df, 'estado_civil', 'estado_civil_cod')
    emprego_codes = column_to_number(df, 'emprego', 'emprego_cod')
    relacionamento_codes = column_to_number(df, 'relacionamento', 'relacionamento_cod')
    raca_codes = column_to_number(df, 'raca', 'raca_cod')
    sexo_codes = column_to_number(df, 'sexo', 'sexo_cod')
    pais_de_origem_codes = column_to_number(df, 'pais_de_origem', 'pais_de_origem_cod')

    print(f"tipo_emprego: {tipo_emprego_codes}")
    print(f"estado_civil: {estado_civil_codes}")
    print(f"emprego: {emprego_codes}")
    print(f"relacionamento: {relacionamento_codes}")
    print(f"raca: {raca_codes}")
    print(f"sexo: {sexo_codes}")
    print(f"pais_de_origem: {pais_de_origem_codes}")

    print(f"df shape (rows, columns): {df.shape}")

    print("df head:")
    print(df.head())

    print("df describe:")
    print(df.describe())

    print("df info:")
    print(df.info())

    # class distribution
    print("df class distribution:")
    print(df.groupby('faixa_renda_anual').size())

    # box and whisker plots
    df.plot(kind='box', subplots=True, layout=(4, 4), sharex=False, sharey=False)
    pyplot.show()

    # histograms
    df.hist()
    pyplot.show()

    # scatter plot matrix
    scatter_matrix(df)
    pyplot.show()


if __name__ == '__main__':
    execute()
