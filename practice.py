import pandas as pd
import numpy as np

my_list = [
    ["Ankit", 22, 2220855, "Software Engineer"],
    ["Shivam", 24, 2220856, "Software Engineer"],
    ["Khushi", 22, 2220857, "Doctor"],
]

list_columns = ["Name", "Age", "RollNumber", "Degisnation"]

data_frame = pd.DataFrame(my_list,columns=list_columns)

print(data_frame)

print(data_frame["Name"])

print(data_frame[["Name", "RollNumber"]])


data_frame["City"] = ["Karnal", "Brampton", "Karnal"]

print(data_frame)