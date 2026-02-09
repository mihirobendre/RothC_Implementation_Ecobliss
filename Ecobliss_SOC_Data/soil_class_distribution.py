import pandas as pd

file_path = 'Ecobliss_stratified_SOC.xlsx'

df = pd.read_excel(file_path)

class_counts = df['Soil_Class'].value_counts(normalize=True)

print(class_counts)
