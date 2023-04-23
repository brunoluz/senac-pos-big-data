import pandas as pd
import matplotlib.pyplot as plt


diabetes = pd.read_csv('diabetes.csv')

print('\n')
print('\n')
print('--------------------DATASET INFO--------------------')
print(diabetes.info())

print('\n')
print('\n')
print('--------------------AGE COLUMN INFO--------------------')
age = diabetes[['Age']]
print(f"min: {age.min()}") 
print(f"max: {age.max()}") 

print('\n')
print('\n')
print('--------------------AGE OLDER THEN 30 INFO--------------------')
age30 = age[age.Age >= 30]
print(f"min: {age30.min()}") 
print(f"max: {age30.max()}") 


print('\n')
print('\n')
print('--------------------CONCLUSION--------------------')
print('\n')
diabetics = diabetes[diabetes.Outcome == 1]
diabetics_glucose = diabetics[['Glucose']]

print('GLUCOSE DIABETICS')
print(diabetics_glucose.describe())

print('\n')
print('NON GLUCOSE DIABETICS')
non_diabetics = diabetes[diabetes.Outcome == 0]
non_diabetics_glucose = non_diabetics[['Glucose']]
print(non_diabetics_glucose.describe())


print("""
A média de glicose das pessoas com diabetes é maior do que das pessoas não diabéticas.
Neste dataset, a média de glicose para diabéticos ficou em 141, enquanto a média para os não diabéticos ficou em 109.

Outro ponto importante para se destacar é que o desvio padrão também é menor para os não diabéticos, ou seja, o valor da glicose dos não diabéticos varia menos.
Neste dataset, o desvio padrão de glicose para diabéticos ficou em 31, enquanto o desvio padrão para os não diabéticos ficou em 26.
""")

print('\n')
print('\n')
print('--------------------MATPLOTLIB--------------------')

age.plot(kind='hist')
plt.show()