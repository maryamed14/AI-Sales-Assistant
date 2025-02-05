import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sales.csv")

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Summary statistics
print("Basic Statistics:\n", df.describe())
print("\nCategory Distribution:\n", df["Category"].value_counts())
print("\nCustomer Segment Distribution:\n", df["Customer_Segment"].value_counts())

# Sales trend over time
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Revenue", data=df, estimator='sum')
plt.title("Sales Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# Sales by category
plt.figure(figsize=(8, 5))
sns.barplot(x=df["Category"], y=df["Revenue"], estimator=sum)
plt.title("Total Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# Sales impact on holidays
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Holiday"], y=df["Revenue"])
plt.title("Sales Impact on Holidays")
plt.xticks(rotation=45)
plt.show()

# Save visualizations (optional)
plt.savefig("data/sales_trends.png")

print("EDA completed! Check the visualizations.")
