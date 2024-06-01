import pandas as pd 
import matplotlib.pyplot as mp 

import sys
sys.path.append ("..")
from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = "/home/azm/projects/birth_data/birth_rate/south_africa/Tables and Appendices.xlsx"

data = pd.read_excel (path, sheet_name ='Appendix G')
df  = pd.DataFrame (data)

lb = []
for i in range (313, 366, 13):
    lb.append(df.iloc[i:i+12, 5].to_list())
lb = sum (lb, [])


gen_bar (lb, 2018, 2022, 0, "South Africa", 0)
generate_graph (lb, 2018, 2022, 1, 1, "South Africa", 0)
