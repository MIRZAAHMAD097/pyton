#DataFrame 1: Student Grades
#ex 1
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis = 1)
print(df1[['Student_ID', 'Average']])
#ex 2

topstudent = df1.loc[df1['Average'].idxmax()]
print("top student: ")
print(topstudent)

#ex 3
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1[['Student_ID', 'Total']])

#ex 4
import matplotlib.pyplot as plt

subject_avg = df1[['Math', 'English', 'Science']].mean()
subject_avg.plot(kind='bar', title='Subject average grades', color= ['skyblue','lightgreen', 'salmon'])
plt.ylabel('Average grade')
plt.xlabel('Subjects')
plt.tight_layout()
plt.show()



#DataFrame 2: Sales Data

#ex1

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales: ")
print(total_sales)

#ex 2

df2['Totalsale'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sale = df2.loc[df2['Totalsale'].idxmax()]
print("the most sales in one day date: ")
print(max_sale[['Date', 'Totalsale']])


#ex 3

percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("percentage change for previous day: ")
print(percentage_change)


#4
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.plot(df2['Date'], df2['Product_A'], label= 'Product_A', marker = 'o')
plt.plot(df2['Date'], df2['Product_B'], label= 'Product_B', marker = 's')
plt.plot(df2['Date'], df2['Product_C'], label= 'Product_C', marker = '^')

plt.title("Daily sale for each product: ")
plt.xlabel("Date")
plt.ylabel("Sales amount")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
