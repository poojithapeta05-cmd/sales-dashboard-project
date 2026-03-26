
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
if not os.path.exists("output"):
    os.makedirs("output")

try:
    # Load dataset
    df = pd.read_csv("sales_data.csv")

    print("Shape of data:", df.shape)
    print(df.head())

    # Clean column names
    df.columns = df.columns.str.strip()

    print("Columns:", df.columns)

    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove missing values
    df = df.dropna(subset=['Sales', 'Profit'])

    print("\nData Loaded Successfully!\n")

    # Total Sales & Profit
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()

    print("\nTotal Sales:", total_sales)
    print("Total Profit:", total_profit)

    # Profit Margin
    df['Profit_Margin'] = (df['Profit'] / df['Sales'].replace(0, 1)) * 100

    # Grouping
    region_sales = df.groupby('Region')['Sales'].sum()
    product_sales = df.groupby('Product')['Sales'].sum()

    print("\nSales by Region:\n", region_sales)
    print("\nSales by Product:\n", product_sales)

    # ------------------ CHARTS ------------------

    # Bar Chart
    plt.figure()
    region_sales.plot(kind='bar', title="Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.savefig("output/region_sales.png")
    plt.show()

    # Pie Chart
    plt.figure()
    product_sales.plot(kind='pie', autopct='%1.1f%%', title="Sales by Product")
    plt.ylabel("")
    plt.savefig("output/product_sales.png")
    plt.show()

    # Line Chart
    daily_sales = df.groupby('Date')['Sales'].sum()

    plt.figure()
    daily_sales.plot(kind='line', title="Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.savefig("output/daily_sales.png")
    plt.show()

    # Save cleaned data
    df.to_csv("cleaned_sales_data.csv", index=False)

    print("\n✅ Cleaned data saved successfully!")

except FileNotFoundError:
    print("Error: sales_data.csv file not found.")

except Exception as e:
    print("Error occurred:", e)