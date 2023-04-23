import pandas as pd

carros = pd.read_csv('Auto2.csv')
print(carros.info())
print(carros.describe())
print(len(carros.index))
heaviest_cars = carros[carros.weight >= 3609]
print(heaviest_cars.describe())