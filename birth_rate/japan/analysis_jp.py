import pandas as pd 
import matplotlib.pyplot as mp 

import sys
sys.path.append ("..")

from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = "/home/azm/projects/birth_data/birth_rate/japan/emb020000.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

lb = []

for i in range (30, 35):
    lb.append (df.iloc[i, 2:].to_list())
lb =sum (lb, [])



br = []

for i in range (65, 70):
    br.append (df.iloc[i, 2:].to_list())
br = sum (br, [])

generate_graph (lb, 2018, 2022, 1, 1, 'Japan', 0)
gen_bar (lb, 2018, 2022, 0, 'Japan', 0)

generate_graph (br, 2018, 2022, 1, 1, 'Japan', 1)
gen_bar (lb, 2018, 2022, 0, 'Japan', 1)
