import pandas as pd 
#extracting the file from local 
df = pd.read_csv('/Users/bollipallipreethichowdary/Downloads/Proj - 1/healthcare_dataset.csv')
print(df)
#Transfromations
#data cleaning
#checking if there are any missing values
df.isnull().sum() 
#duplicate rows - 534 rows
df[df.duplicated()]
#removing duplicate rows
df= df.drop_duplicates()
print(df)
#checking the null values 
df.isnull()
#standardize the name format - converting the first letter in first name and first letter in last name into capitals
#str.title() - string method in pandas used to convert the first letter of each word into capitals
df['Name'] = df['Name'].str.title()
print(df)
#adding length of the stay column 
df['Length of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days
print(df)
# Standardize Gender column
# Step 1: Inspect unique values in the Gender column
print(df['Gender'].unique())
df['Gender'] = df['Gender'].str.strip().str.lower().map({'male': 'M', 'female': 'F'})
print(df)
# Define age group bins and labels
bins = [0, 18, 35, 50, 65, float('inf')]
labels = ['Child', 'Young Adult', 'Adult', 'Senior', 'Elderly']
# Create Age Group column
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
print(df)
df.head(5)
#unique values in insurance provider 
print(df['Insurance Provider'].unique())
#mapping and creating the new column whether the insurance is public or private 
insurance_mapping = {
    'medicare': 'Public',
    'blue cross': 'Private',
    'aetna': 'Private',
    'unitedhealthcare': 'Private',
    'cigna': 'Private'
}
df['Insurance Tier'] = df['Insurance Provider'].str.strip().str.lower().map(insurance_mapping)
print(df)
#dropping the room number 
df.drop(columns='Room Number', inplace=True)
print(df)
#rounding the billing amount to 2 decimal places 
print(df['Billing Amount'])
df['Billing Amount'] = df['Billing Amount'].round(2)
print(df['Billing Amount'])
print(df.columns)
#saving the file in CSV format
df1= df.to_csv("optimized_healthcare_dataset.csv", index=False)