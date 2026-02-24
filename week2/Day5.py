import pandas as pd
import numpy as np

#Q1. Create a dataset of sales data group it by region or product category

data = {
    "Order_Id":[1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Region":["North", "South", "North", "East", "West", "South", "East", "North", "South" ],
    "Product_Category":["Electronics", "Furniture", "Electronics", "Clothing", "Grocerry", "Clothing", "Electronics", "Furniture", "Grocerry"],
    "Sales_Amount":[1200, 1000, 13000, 2300, 1300, 1500, 750, 1290, 1460],
    "Year":[2000, 2001, 2000, 2003, 2004, 2000, 2002, 2003, 2002]
}

df = pd.DataFrame(data)
print("Original Data: \n", df)
'''
#Individual Group
#Group by Region 
sales_by_region = df.groupby("Region")["Sales_Amount"].sum().reset_index()
print(sales_by_region) 
# Group by Product Category 
sales_by_category = df.groupby("Product_Category")["Sales_Amount"].sum().reset_index()
print(sales_by_category)


#Aggregation Function
#Group by region
sales_by_region = df.groupby("Region").agg(
    Total_Sales = ("Sales_Amount", "sum"),
    Average_sales = ("Sales_Amount", "mean"),
    No_of_orders = ("Order_Id", "count")
    ).reset_index()
print(sales_by_region)
#Group by Category
sales_by_category = df.groupby("Product_Category").agg(
    Total_Sales = ("Sales_Amount", "sum"),
    Max_Sales = ("Sales_Amount", "max"),
    Min_Sales = ("Sales_Amount", "min")
    ).reset_index()
print(sales_by_category)


#Q2. Use pivot_table to calculate total sales per region and per year

pivot = df.pivot_table(
    index = ["Year","Region", "Product_Category"],
    values = "Sales_Amount",
    aggfunc=["sum", "min", "max"]
)

pivot.columns= ["Total_Sales", "Min_Sales", "Max_sales"]
pivot = pivot.reset_index()
print(pivot)

df.to_csv("Sales_Data.csv", index=False)
pivot.to_csv("Sales_by_Year.csv", index=False)
'''

#Q3. Create a custom Aggregation function to calculate the varience of each groupp

