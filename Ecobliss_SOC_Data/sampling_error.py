import pandas as pd
import numpy as np

# Path to your Excel file
excel_file = 'ECOBLISS_SOIL_ANALYSIS_2025.xlsx'

# Bulk density mean calculation
sheet_name = 'BULK_DENSITY'
df_bd = pd.read_excel(excel_file, sheet_name=sheet_name)
bd_col = 'Bulk Density (g/cm3)'
bd_mean = df_bd[bd_col].mean(skipna=True)

# SOC mean calculation
sheet_name = 'SOC'  # Change this to your actual sheet name
df_soc = pd.read_excel(excel_file, sheet_name=sheet_name)
soc_col = "Soil Organic Carbon (%)"

# Get unique values in the "FAO LEGEND" column
unique_fao = df_bd["Type"].unique()

print("Unique FAO LEGEND values:")
print(unique_fao)


# If you also want counts of each unique value:
fao_counts = df_bd["Type"].value_counts()

print("\nCounts of FAO LEGEND values:")
print(fao_counts)
print()

avg_bd = df_bd["Bulk Density (g/cm3)"].mean(skipna=True)

for value in unique_fao:
    # Filter rows
    subset = df_soc[df_soc["Type"] == value]
    values = subset["Soil Organic Carbon (%)"].dropna()
    for val in values:
        val = val*avg_bd*30

    # Sample size
    n = len(values)

    # Calculate the average Soil Organic Carbon (%)
    avg_soc = subset["Soil Organic Carbon (%)"].mean(skipna=True)
    variance_of_mean = values.var(ddof=1)
    sem = values.std(ddof=1) / np.sqrt(n)
    print("Average SOC", value, " (t/ha): ", avg_soc*avg_bd*30)
    print("Variance of the mean:", variance_of_mean)
    print("Standard Error of the mean:", sem*avg_bd*30)
    print()

