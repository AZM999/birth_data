import pandas as pd 
import matplotlib.pyplot as mp

# dont remove the following two lines
import sys
sys.path.append ("..")

#import script for generating graph
from scripts.gen_bar import gen_bar


#sys.path.insert ()
path = "/home/azm/projects/birth_data/birth_rate/uk/births_uk.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)
#print (df)

lb = []


for i in range (0, 5):
    lb.append (df.iloc[i, 2:].to_list())
lb = lb[::-1]
lb = sum (lb, [])
#print (lb)

#generate_graph (lb, 2018, 2022, 1, 1, 'UK(England + Wales)', 0)
gen_bar (lb, 2018, 2022, 0, 'UK(England + Wales)', 0)

