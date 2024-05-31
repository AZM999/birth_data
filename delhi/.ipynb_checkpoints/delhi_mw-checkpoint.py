import matplotlib.pyplot as mp 
import pandas as pd 
import seaborn as sb


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
title= " test")
mp.xlabel ('Quarters')
mp.ylabel ('Total ')
for container in ax.containers:
    ax.bar_label(container)
    #plt.tight_layout ()
mp.show ()