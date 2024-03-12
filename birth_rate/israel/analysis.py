#

import pandas as pd 
import matplotlib as mp 
import numpy as np 

import sys
sys.path.append ("..")

from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = "/home/azm/projects/birth_data/birth_rate/israel/Israel_vital_stats_Births.xlsx"
path2 = "/home/azm/projects/birth_data/birth_rate/israel/c1.xls"

data = pd.read_excel (path)
df = pd.DataFrame (data)

data = pd.read_excel (path2)
df2  = pd.DataFrame (data)

s = df2.iloc[40:65, 11].dropna().to_list()
#print (s, len (s))

lb = df.iloc[32:71,11].to_list()

for i in range(1,10):
    lb.append(0)

s = s + lb 
#print (s, len(s))

gen_bar(s, 2018, 2023, 0, "Israel", 0)
generate_graph (s, 2018, 2023, 0, 1, "Israel", 0)
