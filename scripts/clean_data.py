import pandas as pd

print("Loading dataset...")

df = pd.read_excel("data/Online Retail.xlsx")

print("Original Shape:")
print(df.shape)

# Remove missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove negative quantities
df = df[df["Quantity"] > 0]

# Remove negative prices
df = df[df["UnitPrice"] > 0]

# Create Sales Amount
df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("\nCleaned Shape:")
print(df.shape)

df.to_csv(
    "data/clean_retail_data.csv",
    index=False
)

print("\nClean dataset saved.")