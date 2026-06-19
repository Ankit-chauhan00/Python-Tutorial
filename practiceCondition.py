import pandas as pd
import numpy as np

my_dictonary = {
       "Name" :  ["Ankit", "Shivam","Ragnav", "Khushi", "Satyam"],
       "Country":["India", "India", "Canada", "Canada", "USA"],
       "City": ["Karnal", "Karnal", "Brampton", "Vancover", "California"],
       "Age":[22,24,23,22,21],
       "RollNo": [2220855,2220856,2220857,2220858,2220859]
}

data_frame = pd.DataFrame(my_dictonary)

print(data_frame)

data_frame["Income"] = [100000,200000, 300000,400000,1000000]

print(data_frame)

print(data_frame["Name"])

print(data_frame[["Name","Country","Income"]])

print(
    data_frame.loc[
        (data_frame["Country"] == "India") |
        (data_frame["Income"] > 200000)
    ]
)

print(
    data_frame.loc[
        (data_frame["Country"] == "India") &
        (data_frame["Income"] > 200000)
    ]
)

print(
    data_frame.loc[
        (data_frame["Country"] == "India") &
        (data_frame["Income"] > 100000)
    ]
)

print(data_frame.drop(["Age"],axis=1))

print(data_frame.drop(["RollNo","Age"], axis=1))

print(
    data_frame.loc[
        [0,1],
        ["Name", "Country"]
    ]
)

print("Before Actual Data Delete\n")

print(data_frame)

print("After Deletion")

print(data_frame.drop(
    [0,4],
    axis=0
    ))





