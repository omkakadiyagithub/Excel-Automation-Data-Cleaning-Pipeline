import pandas as pd

print("Generating Data Quality Report...")

# Load original dataset
original_df = pd.read_excel("data/Online Retail.xlsx")

# Metrics before cleaning
original_rows = len(original_df)

duplicate_rows = original_df.duplicated().sum()

missing_customerid = original_df["CustomerID"].isnull().sum()

negative_quantity = (original_df["Quantity"] <= 0).sum()

negative_price = (original_df["UnitPrice"] <= 0).sum()

# Load cleaned dataset
clean_df = pd.read_csv("data/clean_retail_data.csv")

clean_rows = len(clean_df)

rows_removed = original_rows - clean_rows

# Create report
report = pd.DataFrame({
    "Metric": [
        "Original Rows",
        "Cleaned Rows",
        "Rows Removed",
        "Duplicate Rows",
        "Missing Customer IDs",
        "Negative Quantities",
        "Negative Prices"
    ],
    "Value": [
        original_rows,
        clean_rows,
        rows_removed,
        duplicate_rows,
        missing_customerid,
        negative_quantity,
        negative_price
    ]
})

print("\n===== DATA QUALITY REPORT =====")
print(report)

report.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print("\ndata_quality_report.csv saved!")