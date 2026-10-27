import pandas as pd

# Load the dataset
df = pd.read_csv("data/hr_dataset.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns.tolist())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)
