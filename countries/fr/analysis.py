# FRance birth rate data 

import pandas as pd 
import matplotlib.pyplot as mp 

import sys
sys.path.append("..")
from scripts.generate_graph import generate_graph
from scripts.gen_bar import gen_bar

path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

df.rename (columns= {'Label': 'time_period', 'Demography - Rate of birth (number of births per 1,000 inhabitants) - France (including Mayotte since 2014)': 'rate_of_birth'}, inplace =True)

tp = df.iloc[3:75, 0].to_list()
br = df.iloc[3:75, 1].to_list()

#print (tp [0])

br = br[::-1]
#generate_graph (br, 2018, 2023, 1, 1, 'France', 1)
gen_bar (br, 2018, 2023, 0, 'France', 1)
# for live births
path1 = "/home/azm/projects/birth_data/birth_rate/fr/live_births_fr.xlsx"

data = pd.read_excel (path1)
df1  = pd.DataFrame (data)
df1.rename (columns= {'label' : 'time_period', 'Demography - Number of live births - Metropolitan France': 'live_births'})
lb = df1.iloc[3:75, 1].to_list ()
lb = lb[::-1]

#generate_graph (lb, 2018, 2023, 1, 1, 'France', 0)
gen_bar (lb, 2018, 2023, 0, 'France', 0)
