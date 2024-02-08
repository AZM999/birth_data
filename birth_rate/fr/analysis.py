# FRance birth rate data 

import pandas as pd 
import matplotlib.pyplot as mp 

path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

df.rename (columns= {'Label': 'time_period', 'Demography - Rate of birth (number of births per 1,000 inhabitants) - France (including Mayotte since 2014)': 'rate_of_birth'}, inplace =True)

tp = df.iloc[3:75, 0].to_list()
br = df.iloc[3:75, 1].to_list()

#print (tp [0])

y_pos = range (len (tp))

bar_br = mp.bar (tp, br)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (month)')
mp.ylabel ('birth rate ')
mp.title ("france- Birth rate 2018-2023")
mp.show ()


## quarter wise data for birth rate

#qtr names 
qtr = []
for i in range (2023, 2017, -1):
    for k in range (4, 0, -1):
        qtr.append (str(i) + "_Q_" + str (k))
qbr =[]

y_pos2 = range (len (qtr))

for i in range (0, 72, 3):
    qbr.append (sum (br [i:i+3]) / 3)

mp.clf()

bar1 = mp.bar (qtr, qbr)
mp.xticks (y_pos2, qtr, rotation=90)
mp.xlabel ('Time Period (Quarter)')
mp.ylabel ('average birth rate ')
mp.title ("france- Birth rate 2018-2023 Quarter wise")
mp.show ()




# for live births
path1 = "/home/azm/projects/birth_data/birth_rate/fr/live_births_fr.xlsx"

data = pd.read_excel (path1)
df1  = pd.DataFrame (data)
df1.rename (columns= {'label' : 'time_period', 'Demography - Number of live births - Metropolitan France': 'live_births'})
lb = df1.iloc[3:75, 1].to_list ()


# qtr wise data for live births
qs =[]

for i in range (0, 72, 3):
    qs.append (sum (lb [i:i+3]))

mp.clf ()

qtr_birth = mp.bar (qtr, qs)
mp.xlabel ('Quarters')
mp.ylabel ('No. of Births in France')
mp.title ('France live births plotted quarterwise 2018-2023')
mp.xticks (y_pos2, qtr, rotation=90)
mp.show()

mp.clf()
lb_monthly = mp.bar (tp, lb)
mp.xlabel ('time period (Month)')
mp.ylabel ('No. of Births')
mp.title ("France- Live Births monthly 2018-2023")
mp.xticks (y_pos, tp, rotation=90)
mp.show ()
