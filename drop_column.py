import pandas as pd
import numpy as np 

my_dictornary = {
    "Name": ["Ankit", "Shivam", "khushi", "Satyam"],
    "RollNo": [2220855, 2220856, 2220857, 2220858],
    "Age":[22,23,22,23],
    "City": ["Karnal", "Brampton", "karnal", "vancover"]
}

data_frame = pd.DataFrame(my_dictornary)

print(data_frame)

print(data_frame["Name"])

print(data_frame[["Name", "City"]])

data_frame["Course"] = ["Computer Science", "Computer Science", "Electrical", "BioTechnologt"]

print(data_frame)

# drop a serise or cloumn tempeary
# axis 1 means it search the colums in x axis
# axis 0 means it seaerch in labels
print(data_frame.drop(["RollNo"],axis=1))
print(data_frame.drop([2], axis=0))

# for  removing the row and column premanetly
# we just have to add implece true

data_frame.drop(["RollNo"], axis=1,inplace=True)
data_frame.drop([2], axis=0, inplace=True)

print(data_frame)

data_frame = pd.DataFrame(my_dictornary)
print(data_frame)

# To select particular Row in a data 
print(data_frame.loc[[0,2]])
# We can use index locatio iloc
print(data_frame.iloc[[1,3]])

#select  particular rows and cloumns
print(data_frame.iloc[[0,3]][["Name", "City"]])
