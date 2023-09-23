import pandas as pd

df_gaming_anxiety = pd.read_csv(filepath_or_buffer="gaminganxiety.csv", delimiter=',', encoding='ANSI')
df_gamint_anxiety_filtered = df_gaming_anxiety[["GADE", "Game", "Platform", "Hours", "Narcissism", "Gender", "Work", "Degree", "GAD_T", "SWL_T", "SPIN_T"]]

df_gamint_anxiety_filtered.to_csv(path_or_buf='gaminganxiety_filtered.csv', sep=',', encoding='utf-8', index=False)