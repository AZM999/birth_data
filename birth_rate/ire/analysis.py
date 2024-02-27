# Ireland birth rate data 

import pandas as pd 
import matplotlib.pyplot as mp
import sys


sys.path.append ("..")
from scripts.gen_bar import gen_bar

path_br = "/home/azm/projects/birth_data/birth_rate/ire/birth_rate_ire.xlsx"
path_lb = "/home/azm/projects/birth_data/birth_rate/ire/live_births_ire.xlsx"

data  = pd.read_excel (path_br)
df_br = pd.DataFrame (data)

data  = pd.read_excel (path_lb)
df_lb = pd.DataFrame(data)

tp = df_br.iloc[:,0]

br = df_br.iloc[:, 3].to_list()
lb = df_lb.iloc[:, 4].to_list()
lb = lb [:: -1]
br = br [:: -1]
lb.append (0)
lb.append (0)
br.append (0)
br.append (0)

print (lb, br)
gen_bar (lb, 2018, 2023, 1, 'Ireland', 0)
gen_bar (br, 2018, 2023, 1, "Ireland", 1)
tp = []

for i in range (2018, 2024):
    for j in range (1, 5):
        tp.append ('Q'+str(j)+' '+str(i))

tp = tp [0:22]

df = pd.DataFrame ({'time_period':tp, 'births':lb, 'birth_rate':br})

df.set_index('time_period')
df = df.sort_values (by =['time_period'])

## quarter wise data birth rte

y_pos = range (len (tp))
bar_br = mp.bar (tp, br)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('birth rate ')
mp.title ("IRELAND- Birth rate 2018-2023Q2")
mp.bar_label (bar_br, labels=br, label_type='edge', rotation=0)
#mp.show ()


## quarter wise data live births

bar_lb = mp.bar (tp, lb)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('Live Births ')
mp.title ("IRELAND- Live Births 2018-2023Q2")
mp.bar_label (bar_lb, labels=lb, label_type='edge', rotation=0)
#mp.show ()

# comparing quarters
tpq = df['time_period'].to_list()
lbq = df['births'].to_list()
brq = df['birth_rate'].to_list()

print (tpq, lbq, brq)

bar_lb_qtr = mp.bar (tpq, lbq)
mp.xticks (y_pos, tpq, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('Live Births ')
mp.title ("IRELAND- Live Births 2018-2023Q2 compared across quarters")
mp.bar_label (bar_lb_qtr, labels=lbq, label_type='edge', rotation=0)
#mp.show ()


bar_br_qtr = mp.bar (tpq, brq)
mp.xticks (y_pos, tpq, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('Birth rate ')
mp.title ("IRELAND- Birth rate 2018-2023Q2 compared across quarters")
mp.bar_label (bar_br_qtr, labels=brq, label_type='edge', rotation=0)
#mp.show ()
