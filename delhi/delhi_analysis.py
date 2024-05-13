import matplotlib as mp 
import pandas as pd 



path = "/home/azm/projects/birth_data/delhi/birt_data_delhi_rti.ods"


import sys
sys.path.append("..")
from generate_graph import generate_graph
#from scripts.gen_bar import gen_bar

#path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

lb = df.iloc[11,2:].to_list() 

print (len(lb), lb)

generate_graph (lb, 2017, 2023, 0, 1, "Delhi combined", 0)
