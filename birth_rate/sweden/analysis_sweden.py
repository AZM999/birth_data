# extract data from the excel file, sort it ascending order and generate graph from script

import pandas as pd 
import matplotlib as mp 

import sys
sys.path.append ("..")
from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = '/home/azm/projects/birth_data/birth_rate/sweden/be0101_manad_befstat_2023m11.xlsx'
data = pd.read_excel (path)

df = pd.DataFrame (data)

lb = []

lb.append (df.iloc[2:14, 3].to_list())
lb.append (df.iloc[19:31, 3].to_list())
lb.append (df.iloc[34:46, 3].to_list())
lb.append (df.iloc[49:61, 3].to_list())
lb = lb [:: -1]
lb = sum (lb, [])

gen_bar (lb, 2020,2023, 0, 'Sweden', 0)
generate_graph (lb, 2020, 2023, 1, 1, "Sweden", 0)
