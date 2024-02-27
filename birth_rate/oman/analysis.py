import pandas as pd
import sys
sys.path.append ("..")


from scripts.gen_bar import gen_bar


path = "/home/azm/projects/birth_data/birth_rate/oman/oman_lb.xlsx"

data = pd.read_excel (path)
df = pd.DataFrame (data)
df['capita'] = df['capita'].replace(',', '', regex=True).astype(int)
lb = df.iloc [:, 1].to_list ()

gen_bar (lb, 2018, 2022, 0, 'Oman', 0)
print (lb)
#print (df)
