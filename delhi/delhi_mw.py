import matplotlib.pyplot as mp 
import pandas as pd 
#import seaborn as sb
import numpy as np 
from generate_graph import generate_graph as gg

path = "/home/azm/projects/birth_data/delhi/delhi_vaccination.ods"
path2 = "/home/azm/projects/birth_data/delhi/birt_data_delhi_rti.ods"


import sys
sys.path.append("..")
#from generate_graph.pivo import generate_graph as gg
#from scripts.gen_bar import gen_bar

#path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)
#print (df)

# Birth data
data1 = pd.read_excel (path2)
df1   = pd.DataFrame (data1)

df1 = df1.drop(df1.index[[2,3,4,5,6,7,8,9,10,11,12]])


df1.index = ['Year', 'Month', 'Total']
dft = df1.transpose()
dft.set_index(['Year' ,'Month','Total'])
dft = dft.iloc[2:,:]

pivoted = dft.pivot(index='Month', columns='Year', values='Total').reset_index()

ax = pivoted.plot.bar(x= 'Month',stacked= False, width=0.8, 
                      title= " Delhi Live Births plotted By month for each year")
mp.xlabel ('Month')
mp.ylabel ('Total Live Births ')
for container in ax.containers:
    ax.bar_label(container)

mp.tight_layout ()
#mp.show ()




#------------------------------- statistical correllation ----------------------------------------------------

pivoted = dft.pivot(index='Month', columns='Year', values='Total').reset_index()
pivoted['sum'] = pivoted.iloc[:,1:].sum(axis = 1)

pivoted['averaged'] = pivoted['sum'].div(7)
pivoted['averaged'] = pivoted['averaged'].apply(np.ceil)

# statistical corellation
#      subtracting actual observed value from the mean of that month for all years 2017 to 2018
#      for ex. 
for i in range (2017, 2024):
    pivoted[str(i)+'_s'] = pivoted[i] - pivoted['averaged']

dfs = pivoted.iloc[:,10:]
dfs['month'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#zero the empty values 
dfs.iloc[3:12, 6] = 0 

ax = dfs.plot.bar(x= 'month',stacked= False, width=0.8, 
                      title= " Delhi Live Births subtracted from average of each month from 2017-2023")
mp.xlabel ('Month')
mp.ylabel ('Total Live Births ')
for container in ax.containers:
    ax.bar_label(container)

mp.tight_layout ()
mp.show()


lb_s = []

for i in range(0,7):
    lb_s.append(dfs.iloc[:,i].to_list())
lb_s = sum (lb_s, [])


gg(lb_s, 2017, 2023, 0, 1, "subtracted from average values for each month and plotted serially", 0, " Live Births")
