#lesson 17
#1

import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25,30,40,45],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

print("first 3 rows: ")
print(df.head(3))

mean_age = df["age"].mean()
print(df[["first_name","city"]])

df["salary"] = np.random.randint(50000, 100000, size = len(df))

print("\nSummary statistics: ")
print(df.describe())


#2

import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print("Sales and Expenses DataFrame:\n", sales_and_expenses)
print("\nMaximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)


#3

import pandas as pd


data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

expenses = expenses.set_index('Category')

max_expenses = expenses.max(axis=1)
min_expenses = expenses.min(axis=1)
avg_expenses = expenses.mean(axis=1)

print("Expenses DataFrame:\n", expenses)

print("\nMaximum expense for each category:\n", max_expenses)
print("\nMinimum expense for each category:\n", min_expenses)
print("\nAverage expense for each category:\n", avg_expenses)