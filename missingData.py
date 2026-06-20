import pandas as pd
import numpy as np


dictonary = {
    "Name": ["Ankit", "Shivam", "Khushi", None, "Satyam"],
    "Country": ["India", "Canada", "India", None, "Canada"],
    "Age":[22,24,22,np.nan,23],
    "City":["Karnal","Karnal","Karnal",None,"Karnal"]
}

df = pd.DataFrame(dictonary)

print(df)

# give the table like which include True or False tht the item is NaN or not
"""

    Name  Country    Age   City
0  False    False  False  False
1  False    False  False  False
2  False    False  False  False
3   True     True   True   True
4  False    False  False  False

"""
print(df.isna())

# gives the cloumn with numer of nan values 
# so we can check any missing values in the cloumn

"""

Name       1
Country    1
Age        1
City       1

"""
print(df.isna().sum())


# checkig that is there is any column with or without null value
"""

Name       True
Country    True
Age        True
City       True

"""
print(df.isna().any())


# Removing null data Works on basis of Rows
# it removes the null rows

"""

     Name Country   Age    City
0    Anki   India  22.0  Karnal
1  Shivam  Canada  24.0  Karnal
2  Khushi   India  22.0  Karnal
4  Satyam  Canada  23.0  Karnal

"""

print(df.dropna())


#adding the threshhold to the columns as 
#threshhold  = 3 means the row should have at least 4 not null values
"""

0   Ankit   India  22.0  Karnal
1  Shivam  Canada  24.0  Karnal
2  Khushi   India  22.0  Karnal
4  Satyam  Canada  23.0  Karnal

see these 3 rows have  have 3 not null values 

"""

print(df.dropna(thresh=3))

# filling nan valuse

print(df.fillna(0))


values ={
    "Name": "Not Provided",
    "Country": "Not Provided",
    "Age": 0,
    "City": "City Not Provided"
}

print(df.fillna(value=values))