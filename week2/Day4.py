import pandas as pd
import numpy as np

#Q1. Drop columns with more than 50% missing values

data = pd.DataFrame({
    "Name":["Laltesh Kumar", "Rahul Roy", "Ayush Kumar", "Ritesh Kumar", "Abhimanyu Kumar", "Abhinandan Kumar", "Aman Kumar"],
    "Age" : [np.nan, np.nan, np.nan, 19, np.nan, np.nan, 21],
    "Score": [80, 63, 79, 92, 82, 87, 89 ]
})

print("Dataset: \n", data)

threshold = len(data) * 0.5
clean_data = data.dropna(axis=1, thresh=threshold)
print("Cleaned Dataset: \n",clean_data)

#Q2. Merge three datasets and analyze relationships between them

data1 = pd.DataFrame({
    "Roll_No.":[1],
    "Name":["Sahil Kumar"],
    "Age":[19]
    
})

data2 = pd.DataFrame({
    "Roll_No.":[1],
    "C_Language":[74],
    "Hindi":[86],
    "Math":[79],
    "English":[88],
    "Basic_Electronics":[86]

})

data3 = pd.DataFrame({
    "Roll_No.":[1],
    

})
print("Dataset 1: \n", data1)
print("Dataset 2: \n", data2)
print("Dataset 3: \n", data3)

merged = data1.merge(data2, on="Roll_No.", how="inner").merge(data3, on="Roll_No.", how="inner")
print("Merged Dataset: \n",merged)

subject_column = ["C_Language", "Hindi", "Math", "English", "Basic_Electronics"]
merged["Percentage"] = merged[subject_column].sum(axis=1) / (100*len(subject_column)) * 100

print("Merged Dataset with Percentage: \n", merged)

#Q3. Convert categorical data to numerical using on-hot encoding

