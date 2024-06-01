import pandas as pd
from generate_graph import *


# Test
path = "/home/azm/projects/birth_data/birth_rate/uk/births_uk.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)
df.head()
lb = []

for i in range (0, 5):
    lb.append (df.iloc[i, 2:].to_list())

lb = lb[::-1]
lb = sum (lb, [])
generate_graph (lb, 2018, 2022, 1, 0, 'UK (England + Wales)', 0)
