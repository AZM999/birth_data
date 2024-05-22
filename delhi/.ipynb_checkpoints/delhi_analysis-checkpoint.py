import matplotlib.pyplot as mp 
import pandas as pd 
from generate_graph import generate_graph as gg


path  = "/home/azm/projects/birth_data/delhi/delhi_vaccination.ods"
path2 = "/home/azm/projects/birth_data/delhi/birt_data_delhi_rti.ods"

#import sys
#sys.path.append("..")
#from generate_graph import generate_graph
#from scripts.gen_bar import gen_bar

#path = "/home/azm/projects/birth_data/birth_rate/fr/birth_rate_fr.xlsx"

# vaccination data
data = pd.read_excel (path)
df  = pd.DataFrame (data)
#print (df)

# Birth data
data1 = pd.read_excel (path2)
df1   = pd.DataFrame (data1)

print (df1.iloc[11, 2:])
df1 = df1.iloc[11, 2:]


# set index for vaccinations
df = df.drop(columns=['label'])
df.set_index(['year', 'month'])

s2 = df.groupby(['year', 'month']).sum()


# extract dose1, dose2, precautionary doses and total of all
d1 = s2.dose1.to_list()
d2 = s2.dose2.to_list()
prd = s2.Precaution_dose.to_list()
total_doses = s2.total.to_list()

# plot total dose
#print (total_doses, len(total_doses))
total_doses = total_doses[0:36]
temp = [0] * 12*4 + total_doses
#print(total_doses, len(total_doses))
#gg(total_doses, 2021, 2023, 0, 1, "delhi vaccinations", 0, " ")


# xlabel months
tp = []
for i in range (2017, 2024):
    for m in range (1,13):
        tp.append(str(i) + '-' + str(m))
        

# Birth data
print(df1.to_list())

#gg(df1.to_list(), 2017, 2023, 0, 1, "Delhi", 0, "Live Births")

# vaccinations vs live births 

fig, ax1 = mp.subplots()

y_pos = range (len (tp))
color = 'tab:blue'
ax1.set_xlabel ('Time Period (months)')
ax1.set_ylabel ('Live Births (total)', color=color)
figure = ax1.bar (tp, df1.to_list(), color=color)
ax1.tick_params(axis='y', labelcolor=color)
mp.xticks (y_pos, tp, rotation=90)
mp.bar_label (figure, labels=df1.to_list(), label_type='edge', rotation=60)


# vaccination data

ax2 = ax1.twinx() 
color = 'tab:red'
ax2.set_ylabel('Vaccinations (total)', color=color)  # we already handled the x-label with ax1
ax2.plot(tp, temp, color=color)
ax2.tick_params(axis='y', labelcolor=color)


mp.title('Live Births Vs Vaccinations visualised')
#fig.tight_layout()

mp.show()




#------------------------------- live births vs Vaccinations (slided 9 months)--------------------------



# vaccinations vs live births with vaccinations slided 9 months

temp1 = [0]*9 + temp [0:75]
temp1, len (temp1)

fig, ax1 = mp.subplots()

y_pos = range (len (tp))
color = 'tab:blue'
ax1.set_xlabel ('Time Period (months)')
ax1.set_ylabel ('Live Births (total)', color=color)
figure = ax1.bar (tp, df1.to_list(), color=color)
ax1.tick_params(axis='y', labelcolor=color)
mp.xticks (y_pos, tp, rotation=90)
mp.bar_label (figure, labels=df1.to_list(), label_type='edge', rotation=60)


# vaccination data

ax2 = ax1.twinx() 
color = 'tab:red'
ax2.set_ylabel('Vaccinations (total)', color=color)  # we already handled the x-label with ax1
ax2.plot(tp, temp1, color=color)
ax2.tick_params(axis='y', labelcolor=color)


mp.title('Live Births Vs Vaccinations visualised (vaccinations slided 9 months)')


mp.show()
