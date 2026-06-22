import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== FIRST 5 ROWS =====")
print(df.head())