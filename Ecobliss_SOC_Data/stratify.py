import pandas as pd

# ====== Read, process	======
file_path = "Ecobliss_SOC_Data.xlsx"

bd_df = pd.read_excel(file_path, sheet_name = 'Bulk_Density')
#print(bd_df.head())
average_bd = bd_df['Bulk Density (g/cm3)'].mean()
#print(average_bd)

soc_df = pd.read_excel(file_path, sheet_name = 'Organic_Carbon')


# ====== Filter by depth ======
soc_0_15 = soc_df[soc_df['Depth (cm)'].str.contains('0 -', na=False)]
soc_15_30 = soc_df[soc_df['Depth (cm)'].str.contains('30', na=False)]

#print(soc_0_15.head())
#print(soc_15_30.head())

# ====== Compute SOC by depth layer ======

# 0-15cm depth layer
rows_list = []
for index, row in soc_0_15.iterrows():
	soc_for_layer = row['Soil Organic Carbon (%)'] * average_bd * 15
	row['SOC (t/ha)'] = soc_for_layer
	rows_list.append(row)

soc_0_15 = pd.DataFrame(rows_list)
#print(soc_0_15.head())

# 15-30cm depth layer
rows_list = []
for index, row in soc_15_30.iterrows():
    soc_for_layer = row['Soil Organic Carbon (%)'] * average_bd * 15
    row['SOC (t/ha)'] = soc_for_layer
    rows_list.append(row)

soc_15_30 = pd.DataFrame(rows_list)
#print(soc_15_30.head())


# ====== Combine them for total SOC  ======

rows_list = []
for index, row_0_15 in soc_0_15.iterrows():
	sample_id = row_0_15['Sample ID']
	row_15_30 = soc_15_30[soc_15_30['Sample ID'] == sample_id]
	#print(row_15_30)
	new_soc_stock = row_0_15['SOC (t/ha)'] + row_15_30['SOC (t/ha)']
	
	cleaned_row = row_0_15.drop(['Depth (cm)', 'No.', 'Soil Organic Carbon (%)'])
	cleaned_row['SOC (t/ha)'] = new_soc_stock.item()
	rows_list.append(cleaned_row)


# ====== Define new classification function ======
def classify_soc_stock(soc_stock):
    if soc_stock < 10:
        return "Severely Degraded"
    elif 10 <= soc_stock < 30:
        return "Degraded"
    elif 30 <= soc_stock < 50:
        return "Moderate"
    elif 50 <= soc_stock < 70:
        return "Fertile"
    elif soc_stock >= 70:
        return "Very Fertile"
    else:
        return "N/A"

# ====== Apply classification to SOC column ======
new_df = pd.DataFrame(rows_list)
new_df['Soil_Class'] = new_df['SOC (t/ha)'].apply(classify_soc_stock)
#print(new_df.head())

file_name = 'Ecobliss_stratified_SOC.xlsx'
new_df.to_excel(file_name, index=False)

# ====== Calculate average of each strata ======
print("Average SOC (tons/ha) by strata: ")

all_soil_classes = new_df['Soil_Class'].unique().tolist()
#print(all_soil_classes)

for soil_class in all_soil_classes:
	filtered = new_df[new_df['Soil_Class'] == soil_class]
	#print(filtered)
	average_soc = filtered['SOC (t/ha)'].mean()
	print("	", soil_class, ": ", average_soc)


'''
filtered = new_df[new_df['Soil_Class'] == "Degraded"]
print(filtered)
average_soc = filtered['SOC (t/ha)'].mean()
print("	Severely Degraded: ", average_soc)
'''


