import pandas as pd 
import matplotlib.pyplot as mp 

import sys
sys.path.append ("..")
from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar


path = "/home/azm/projects/birth_data/birth_rate/turk/births by month.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

lb = []

for i in range (17, 22):
    lb.append (df.iloc[i, 2:].to_list())


lb = sum (lb, [])

gen_bar (lb, 2018, 2022, 0, "Turkiye", 0)
generate_graph (lb, 2018, 2022, 1, 1, "Turkiye", 0)
