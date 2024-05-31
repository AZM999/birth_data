
import matplotlib.pyplot as mp 
import pandas as pd 

path = "/home/azm/projects/birth_data/delhi/birth_bmc_f⁄s_ward.ods"
path2 = "/home/azm/projects/birth_data/delhi/birth_death_bmc_f⁄s_ward.ods"

import sys
sys.path.append("..")
from generate_graph import generate_graph as gg
#from scripts.gen_bar import gen_bar

#path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)
df = df.iloc[2:,:]

col = ['month', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

df.columns = col


### month wise plot to compare each month

ax = df.plot.bar(x= 'month',stacked= False, width=0.8, 
                      title= " Mumbai Live Births plotted By month for each year")
mp.xlabel ('Month')
mp.ylabel ('Total Live Births ')
for container in ax.containers:
    ax.bar_label(container)

mp.tight_layout ()
mp.show ()


## PLot Live births month wise for each year seraially
lb = []

for i in range(1,8):
    lb.append(df.iloc[:,i].to_list())
lb = sum (lb, [])

tp = []
for i in range (2017, 2024):
    for m in range (1,13):
        tp.append(str(i) + '-' + str(m))

gg(lb, 2017, 2023, 0, 1, "Mumbai F_south ward Live Births", 0, " Live Births")


# Death data
data2 = pd.read_excel (path2)
df2  = pd.DataFrame (data2)
df2 = df2.iloc[1:,:]
df2.columns= col

dc = []
for i in range(1,8):
    dc.append(df2.iloc[:,i].to_list())
dc = sum (dc, [])

gg(dc, 2017, 2023, 0, 1, "Mumbai F_south ward Total Death for each Month", 0, "Deaths")
