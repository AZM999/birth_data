import pandas as pd 
import matplotlib.pyplot as mp 

path = "/home/azm/projects/birth_data/birth_rate/south_africa/Tables and Appendices.xlsx"

data = pd.read_excel (path, sheet_name ='Appendix G')
df  = pd.DataFrame (data)

lb = []
for i in range (365, 312, -13):
    lb.append(df.iloc[i:i+12, 5].to_list())
lb = sum (lb, [])

tp = []
for i in range(2022, 2017, -1):
    for k in range (12, 0, -1):
        tp.append(str(i)+'-'+str(k))

qtr = []
for i in range (2022, 2017, -1):
    for k in range (4, 0, -1):
        qtr.append (str(i) + "Q" + str (k))
        
qs = []
for i in range (0, 60, 3):
    qs.append (sum (lb [i:i+3]))

    
#plotting results month wise
y_pos = range (len (tp))
births = mp.bar (tp, lb)
mp.xlabel ('Month')
mp.ylabel ('No. of Births')
mp.title ('South Africa - live births 2018-2022')
mp.xticks (y_pos, tp, rotation=90)
mp.show()

# plotting results quarter wise

mp.clf()
y_pos2 = range (len (qtr))
births = mp.bar (qtr, qs)
mp.xlabel ('Quarter')
mp.ylabel ('No. of Births ')
mp.title ('South Africa - live births 2018-2022 Quarter wise')
mp.xticks (y_pos2, qtr, rotation=90)
mp.show()