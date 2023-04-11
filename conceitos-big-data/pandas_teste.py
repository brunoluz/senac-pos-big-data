import pandas as pd
diabetic_data = pd.read_csv('diabetic_data.csv')
print(diabetic_data.info())
print(diabetic_data.describe())

coluna_age = diabetic_data['age']
print(coluna_age.describe())

subset = diabetic_data[['encounter_id', 'race', 'time_in_hospital']]
print(subset.info())
print(subset.describe())

subset_time = subset[subset.time_in_hospital > 3]
print(subset_time.describe())
