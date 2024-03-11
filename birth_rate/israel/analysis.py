#

import pandas as pd 
import matplotlib as mp 
import numpy as np 

import sys
sys.path.append ("..")

from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = "/home/azm/projects/birth_data/birth_rate/israel/Israel_vital_stats_Births.xlsx"

data = pd.read_excel (path)
df = pd.DataFrame (data)

lb = df.iloc[32:71,11].to_list()

for i in range(1,10):
    lb.append(0)

print (lb, len(lb))

gen_bar(lb, 2020, 2023, 0, "Israel", 0)
generate_graph (lb, 2020, 2023, 0, 1, "Israel", 0)
