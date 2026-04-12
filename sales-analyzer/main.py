import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create revenue column using NumPy
df["revenue"] = np.multiply(df["quantity"], df["price"])

# Total revenue
total_revenue = np.sum(df["revenue"])

# Best selling product
best_product = df.groupby("product")["quantity"].sum().idxmax()

# Monthly sales
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["revenue"].sum()

# Average order value
avg_order = np.mean(df["revenue"])

# Output
print("Total Revenue:", total_revenue)
print("Best Product:", best_product)
print("Average Order Value:", avg_order)

print("\nMonthly Sales:")
print(monthly_sales)