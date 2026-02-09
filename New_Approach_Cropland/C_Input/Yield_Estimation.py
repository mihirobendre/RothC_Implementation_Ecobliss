import pandas as pd
import numpy as np

df = pd.read_csv("Ghana_Crop_Data.csv")
#print(df.head())
#print(df["DISTRICT"].unique())

##########################
######### MAIZE ##########
##########################

crop = "MAIZE"
region = "UPPER WEST"
df = df[df["REGION"] == region]

print("All types of crops in dataset: ")
print(df["CROP"].unique())
print()

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")

print()

##########################
######### RICE ##########
##########################

df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "RICE"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")

print()
##########################
######### YAM ##########
##########################

df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "YAM"
region = "UPPER WEST"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]      
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)
    
clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)    

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

##########################
######### SORGHUM ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "SORGHUM"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

##########################
######### MILLET ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "MILLET"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

##########################
######### GROUNDNUT ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "GROUNDNUT"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

##########################
######### COWPEA ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "COWPEA"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

##########################
######### SOYABEAN ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "SOYABEAN"
region = "UPPER WEST"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

