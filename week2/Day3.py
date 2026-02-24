import pandas as pd

#Q1. Load a local Excel file and  explore ites structure

df_excel = pd.read_excel("/home/sid-neon/Downloads/MonthlyBudget-AutoSUM-01.xlsx")
df_csv = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")



print("1st 5 Coloum: \n",df_csv.head())
print("last 5 Column: \n",df_csv.tail())

print("1st 5 Coloum: \n",df_excel.head())
print("last 5 Column: \n",df_excel.tail())


#Q2. Create a data frame from dictionary and add a new calulated coloumn

data = {
    "Name":["Alice", "shivam", "Ritesh", "Mritunjay", "Rahul"],
    "Age":[21, 19, 16, 21, 18],"Salary":[110000, 250000, 300000, 600400, 96000]
    }
df = pd.DataFrame(data)

#adding new column
df["Salary after Tax"] = df["Salary"] * 0.91

print(df)

#Q3. Save filtered data to a new CSV file

data = {
    "Name":["Alice", "shivam", "Ritesh", "Mritunjay", "Rahul"],
    "Age":[21, 19, 16, 21, 18],"Salary":[110000, 250000, 300000, 600400, 96000]
    }
df = pd.DataFrame(data)

#save in csv file

df.to_csv("EmployeData.csv", index=False)
df.to_excel("EmployeData.xlsx", index=False)