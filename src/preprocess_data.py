import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/sample_sales.csv")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# Add new features
df["Month"] = df["Date"].dt.month  # Extract month for trend analysis
df["Year"] = df["Date"].dt.year    # Extract year
df["Day_of_Week"] = df["Date"].dt.day_name()  # Extract day of the week

# Define a list of holidays (example)
holidays = {"2024-01-01": "New Year", "2024-07-04": "Independence Day", "2024-12-25": "Christmas"}
df["Holiday"] = df["Date"].astype(str).map(holidays).fillna("None")

# Simulate promotions/events (random assignment for demonstration)
promotion_days = np.random.choice(df["Date"], size=int(len(df) * 0.1), replace=False)
df["Promotion_Event"] = df["Date"].isin(promotion_days)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Fill missing values if necessary (optional, based on dataset inspection)
df.fillna(method="ffill", inplace=True)  # Forward fill for missing values

# Save cleaned dataset
df.to_csv("data/cleaned_sales.csv", index=False)

print("Data preprocessing complete. Cleaned dataset saved as 'cleaned_sales.csv'!")
