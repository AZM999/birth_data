import pandas as pd 
import matplotlib.pyplot as mp 

import sys
sys.path.append ("..")
from scripts.generate_graph import generate_graph

from scripts.gen_bar import gen_bar


path = "/home/azm/projects/birth_data/birth_rate/south_korea/Live_Births_by_Sex_and_Month_for_city__county__and_district_20240128160644.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

lst = df.iloc[1, 1:181].to_list()
lb = lst[0:180:3]
lb = lb [:: -1]

gen_bar (lb, 2018, 2022, 0, 'South Korea', 0)
generate_graph (lb, 2018, 2022, 1, 1, "South Korea", 0)
