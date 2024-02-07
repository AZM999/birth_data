# live births

import pandas as pd 
import matplotlib.pyplot as mp 

path = "/home/azm/projects/birth_data/birth_rate/fr/live_birthsfr.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)


