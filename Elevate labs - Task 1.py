#importing necessary libraries, pandas in this case
import pandas as pd

#loading the dataset
df = pd.read_csv(r"C:\Elevate labs Task 1\Task 1\Car details Cardekho (Raw Dataset).csv")

#initial data exploration
print(df.head()) #prints the first 5 rows of the dataset
print(df.info()) #prints the information about the dataset including data types and non-null counts
print(df.isnull().sum()) #prints the number of null values in each column
print('Dupicates: ', df.duplicated().sum()) #this will print the number of duplicates

#STEP 1 - handling missing values
#checking for nulls
print(df.isnull().sum()) #this prints the no. of null values in the dataset

#dropping rows with null values
df.dropna(inplace=True) #this will drop all rows with null values

#STEP 2 - removing duplicates
df = df.drop_duplicates() #this will remove all duplicate rows from the dataset

#STEP 3 - Cleaning categorical/text columns
# Standardizing fuel type and seller type
df['fuel'] = df['fuel'].str.lower().str.strip()
df['seller_type'] = df['seller_type'].str.lower().str.strip()

#STEP 4 - Convert columns to proper data types
# Clean and convert mileage column
df['mileage'] = df['mileage'].str.replace(' kmpl', '', regex=False)
df['mileage'] = df['mileage'].str.replace(' km/kg', '', regex=False)
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

# Clean and convert engine column
df['engine'] = df['engine'].str.replace(' CC', '', regex=False)
df['engine'] = pd.to_numeric(df['engine'], errors='coerce')

# Clean and convert max_power
df['max_power'] = df['max_power'].str.replace(' bhp', '', regex=False)
df['max_power'] = pd.to_numeric(df['max_power'], errors='coerce')

#STEP 5 - Standardize column names
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

#STEP 6 - Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False) #this will save the cleaned dataset to a new csv file

print('random samples: ',df.sample(10)) 
print('df description: ',df.describe()) #this will print the description of the dataset including mean, std, min, max, etc.