import pandas as pd
import numpy  as np
from data import people

PeopleDataFrame = pd.DataFrame(people)
print(PeopleDataFrame)

print(PeopleDataFrame.iloc[[7,8,9]][["name", "country", "age"]])

selectedRows = PeopleDataFrame.iloc[[0,2,4,6,7]]

print(
    selectedRows.loc[
        selectedRows["age"] > 30,
        ["name", "country", "age"]
    ]
)

print(
    PeopleDataFrame.loc[
       (PeopleDataFrame["country"] == "India") &
       (PeopleDataFrame["age"] >= 25),
       ["name", "country", "age"]
    ]
)