import pandas as pd
import numpy as np
from data import people
from data import people_data

# data = {
#     "Name": ["Ankit", "Shivam", "Khushi", "Satyam", "Bharat"],
#     "RollNo":[2220855,2220856,2220857, 2220858,2220859],
#     "City": ["Karnal", "Brampton", "Indiana", "Vancover", "Karnal"],
#     "Salart":[1000000, 2222200, 2222020, 1000000, 10000000],
# }

#d = pd.DataFrame(people,)

columns = ["Name", "City", "Country", "Phone", "Age"]

d = pd.DataFrame(people_data, columns=columns)
# print(d)

# print(d[["Name", "City"]])

d["Designation"] = ["Doctor","Doctor","Doctor","Doctor","Doctor","Doctor","Doctor","Doctor","Doctor","Doctor",]

print(d)