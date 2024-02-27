## Script to generate graph for countries quarterwise, month-wise and sorted for comparision

# Data must be of specific format :
# month-wise sorted ascendingly for month month-wise
# 

## import libraries
import matplotlib.pyplot as mp
import pandas as pd


# generate plot from the data
def plot_bar (x_data, y_data, x_label, y_label, title, ):
    # generate a plot with values on top and graph width adjusted
    y_pos = range (len (x_data))
    mp.clf()
    figure = mp.bar (x_data, y_data, )
    mp.xlabel (x_label)
    mp.ylabel (y_label)
    mp.title (title)
    mp.xticks (y_pos, x_data, rotation=90)
    mp.bar_label (figure, labels=y_data, label_type='edge', rotation=0)
    mp.show ()


# Main driver code for generating monthly names, quarter names, and generating
# plots comparing the values month wise comparision and quaterly comparision for 
# all years

def generate_graph (data, from_, to, quarterly, monthly, country, br=False, save=False):

    total_records = 12 * (int(to)+1 - int (from_))

    #generate y_values for time period 
    if monthly==1 or monthly == True:

        tp = []
        for i in range (from_, to+1):
            for m in range (1,13):
                tp.append(str (i) +'-'+ str(m))

        tp_m = []
        for i in range (from_, to+1):
            for m in range (1,13):
                tp_m.append(str(m) + '-' + str(i))

        # plot monthly data

        plot_bar (tp, data, 'Time Period (months)', 'Total No. of Births',
                  str(country)+' - Live Births '+str(from_)+'-'+str(to)+' Monthly')
        
        # compare each month
        # df1 = pd.DataFrame ({'time_period':tp_m, 'data': data})
        # df1.set_index ('time_period')
        # df1 = df1.sort_values (by=['time_period'])
        # print (df1)



    # check if quarterly required

    if quarterly==1 or quarterly==True:

        # synthetic quarter names
        qtr = []
        for i in range (from_, to+1):
            for j in range (1, 5):
                qtr.append ('Q'+str(j)+'-'+str(i))

        # sum values for quarter-wise results
        if br == 1 or br == True:
            #calculate avg birth rate for each quarter
            qs = []
            print (total_records)
            for i in range (0, total_records, 3):
                qs.append (sum (data [i:i+3]))
        else:
            qs = []
            print (total_records)
            for i in range (0, total_records, 3):
                qs.append (sum (data [i:i+3]))

        df2 = pd.DataFrame ({'quarter':qtr, 'data': qs})
        df2.set_index ('quarter')
        df2 = df2.sort_values(by=['quarter'])
        qt = df2['quarter'].to_list ()
        dat = df2['data'].to_list ()

        plot_bar (qt, dat, 'Time period (Quarter)', 'Total No. of Births', 
                  str(country)+' - Live Births '+str(from_)+'-'+str(to)+' Quaterly')





        


# Test
path = "/home/azm/projects/birth_data/birth_rate/uk/births_uk.xlsx"

data = pd.read_excel (path)
df  = pd.DataFrame (data)
df.head()
lb = []

for i in range (0, 5):
    lb.append (df.iloc[i, 2:].to_list())

lb = lb[::-1]
lb = sum (lb, [])


#generate_graph (lb, 2018, 2022, 1, 0, 'UK (England + Wales)', 0)

 

