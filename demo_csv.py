# Lecture fichier csv

import pandas as pd

csv_file = 'file.csv'
dataCSV = pd.read_csv(csv_file)
print(dataCSV.head())