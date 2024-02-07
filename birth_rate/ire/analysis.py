# Ireland birth rate data 

import pandas as pd 
import matplotlib.pyplot as mp 

path_br = "/home/azm/projects/birth_data/birth_rate/ire/birth_rate_ire.xlsx"
path_lb = "/home/azm/projects/birth_data/birth_rate/ire/live_births_ire.xlsx"

data  = pd.read_excel (path_br)
df_br = pd.DataFrame (data)

data  = pd.read_excel (path_lb)
df_lb = pd.DataFrame(data)

tp = df_br.iloc[:,0]

br = df_br.iloc[:, 3]
lb = df_lb.iloc[:, 4]

## quarter wise data birth rate

y_pos = range (len (tp))
bar_br = mp.bar (tp, br)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('birth rate ')
mp.title ("IRELAND- Birth rate 2018-2023Q2")
mp.show ()


## quarter wise data live births

bar_lb = mp.bar (tp, lb)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('Live Births ')
mp.title ("IRELAND- Live Births 2018-2023Q2")
mp.show ()