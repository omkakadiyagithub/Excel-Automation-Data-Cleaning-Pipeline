import pandas as pd

print("Loading cleaned dataset...")

df = pd.read_csv("data/clean_retail_data.csv")

# KPIs
total_revenue = df["Sales"].sum()

total_orders = df["InvoiceNo"].nunique()

total_customers = df["CustomerID"].nunique()

average_order_value = total_revenue / total_orders

top_country = (
    df.groupby("Country")["Sales"]
    .sum()
    .idxmax()
)

# Create KPI DataFrame
kpi_df = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Top Revenue Country"
    ],
    "Value": [
        total_revenue,
        total_orders,
        total_customers,
        average_order_value,
        top_country
    ]
})

print("\n===== KPI SUMMARY =====")
print(kpi_df)

# Save KPIs
kpi_df.to_csv(
    "reports/kpi_summary.csv",
    index=False
)

print("\nkpi_summary.csv saved!")