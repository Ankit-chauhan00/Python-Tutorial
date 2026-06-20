import pandas as pd
import numpy as np

#employee dataframe
employee_dataframe = pd.DataFrame({
    "Name":["Ankit","Shivam", "Khushi", "Peter"],
    "employee_id": [1,2,3,4],
    "Department": ["It", "Sales", "Management", "Finance"]
})


#Salary dataframe
employee_salaries = pd.DataFrame({
    "employee_id": [1,2,6,7],
    "Salary": [200000,230000,430000,233000],
    "bonus": [5000, 2000, 10000, 10000]
})


print(employee_dataframe)
print(employee_salaries)

# merging these two data Frames 
merged_data_outer =  pd.merge(employee_salaries,employee_dataframe, on="employee_id", how='outer')
merged_data_inner =  pd.merge(employee_salaries,employee_dataframe, on="employee_id", how='outer')

print(merged_data_outer,"\n")

missing_values = {
    "Salary": 0.0,
    "bonus": 0.0,
    "Name": "Not Provided",
    "Department": "None"

    }

print("Outer Join\n")
print(merged_data_inner.fillna(value=missing_values),"\n")

print("Inner Join\n")
print(merged_data_inner.fillna(value=missing_values))


