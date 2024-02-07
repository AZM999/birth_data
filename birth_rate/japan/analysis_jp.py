import pandas as pd 
import matplotlib.pyplot as mp 

path = "/home/azm/projects/birth_data/birth_rate/japan/emb020000.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)

lb = []

for i in range (34, 29, -1):
    lb.append (df.iloc[i, 2:].to_list())
lb =sum (lb, [])

br = []

for i in range (69, 64, -1):
    br.append (df.iloc[i, 2:].to_list())
br = sum (br, [])

tp = []
for i in range(2022, 2017, -1):
    for k in range (12, 0, -1):
        tp.append(str(i)+'-'+str(k))
        

qtr = []
for i in range (2022, 2017, -1):
    for k in range (4, 0, -1):
        qtr.append (str(i) + "Q" + str (k))

qs =[]

for i in range (0, 60, 3):
    qs.append (sum (lb [i:i+3]))
    
qbr = []

for i in range (0, 60, 3):
    qbr.append (sum (br [i:i+3]) / 3)

y_pos = range (len (tp))
y_pos2 = range (len (qtr))

# quarter-wise-births and birth rate
qtr_birth = mp.bar (qtr, qs)
mp.xlabel ('Quarters')
mp.ylabel ('No. of Births')
mp.title ('JAPAN - live births plotted quarterwise 2018-2022')
mp.xticks (y_pos2, qtr, rotation=90)
mp.show()

qtr_br = mp.bar (qtr, qbr)
mp.xlabel ('Quarters')
mp.ylabel ('average birth rate')
mp.title ('JAPAN - average birth rate plotted quarterwise 2018-2022')
mp.xticks (y_pos2, qtr, rotation=90)
mp.show()

# month-wise-plots

bar_br = mp.bar (tp, lb)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (month)')
mp.ylabel ('No of births ')
mp.title ("JAPAN - Live Birth 2018-2022")
mp.show ()

bar_br = mp.bar (tp, br)
mp.xticks (y_pos, tp, rotation=90)
mp.xlabel ('Time Period (month)')
mp.ylabel ('birth rate ')
mp.title ("JAPAN - Birth rate plotted month wise 2018-2022")
mp.show ()