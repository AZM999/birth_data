# 

import pandas as pd 
import matplotlib.pyplot as plt 



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


##
## gen_bar 
def gen_bar (data, from_, to, isquarterly, country, br):

    total_records = 12 * (int(to)+1 - int (from_))


    if br==1 or br== True:
        title = "Birth rate"
    else:
        title = "Live Births"

    #generate y_values for time period 
        # plot monthly data

        
        # compare each month
        # df1 = pd.DataFrame ({'time_period':tp_m, 'data': data})
        # df1.set_index ('time_period')
        # df1 = df1.sort_values (by=['time_period'])
        # print (df1)



    # check if quarterly required

    if isquarterly != 1 or isquarterly != True:

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
                qs.append ( round(sum (data [i:i+3]) / 3, 3))
        else:
            qs = []
            print (total_records)
            for i in range (0, total_records, 3):
                qs.append (sum (data [i:i+3]))

        # we have values with quarter 
        qs1 = qs.copy ()
        new_ = []
        for i in range (from_, to+1):
            new_.append([str (i) , qs1 [0], qs1[1], qs1[2], qs1[3]])
            #print (qs1)
            del qs1[0:4]

        df2 = pd.DataFrame ({'quarter':qtr, 'data': qs})
        df2.set_index ('quarter')
        df2 = df2.sort_values(by=['quarter'])
        qt = df2['quarter'].to_list ()
        dat = df2['data'].to_list ()
        print (df2)
        # df2 = pd.DataFrame (new_, columns=['Year', 'Q1', 'Q2', 'Q3', 'Q4'])

        #d.plot (x= 'qtr', kind= 'bar', stacked= False, 
        #          title= 'quarter-wise birth rate')       
        dt = dat.copy()
        print (dt)
        qws = []
        for i in range (1,5):
            a = [['Quarter '+str (i)]]
            a.append (dt [0:to-from_+1])
            qws.append(sum (a, []))
            del dt[0:to-from_+1]

        print (qws)
        col = ['qtr']
        for i in range (from_, to+1):
            col.append (str(i))

        df3 = pd.DataFrame (qws,columns= col)

        ax = df3.plot.bar(x= 'qtr',stacked= False, width=0.8,
                  title= country+" -"+title+" Quarters compared")
        plt.xlabel ('Quarters')
        plt.ylabel ('Total '+title)
        for container in ax.containers:
            ax.bar_label(container)
        #plt.tight_layout ()
        plt.show ()


        #df2.set_index ('quarter')
        #df2 = df2.sort_values(by=['quarter'])
        #qt = df2['quarter'].to_list ()
        #dat = df2['data'].to_list ()


        #for i in range (0, 4 * (to-from_ ), to-from_+1 ):
        #print (df2.iloc [i:i+to-from_+1], 1)
    else:
        qs = data.copy ()
        qtr = []
        for i in range (from_, to+1):
            for j in range (1, 5):
                qtr.append ('Q'+str(j)+'-'+str(i))

        # we have values with quarter 
        qs1 = qs.copy ()
        new_ = []
        for i in range (from_, to+1):
            new_.append([str (i) , qs1 [0], qs1[1], qs1[2], qs1[3]])
            #print (qs1)
            del qs1[0:4]

        df2 = pd.DataFrame ({'quarter':qtr, 'data': qs})
        df2.set_index ('quarter')
        df2 = df2.sort_values(by=['quarter'])
        qt = df2['quarter'].to_list ()
        dat = df2['data'].to_list ()
        print (df2)
        # df2 = pd.DataFrame (new_, columns=['Year', 'Q1', 'Q2', 'Q3', 'Q4'])

        #d.plot (x= 'qtr', kind= 'bar', stacked= False, 
        #          title= 'quarter-wise birth rate')       
        dt = dat.copy()
        print (dt)
        qws = []
        for i in range (1,5):
            a = [['Quarter '+str (i)]]
            a.append (dt [0:to-from_+1])
            qws.append(sum (a, []))
            del dt[0:to-from_+1]

        print (qws)
        col = ['qtr']
        for i in range (from_, to+1):
            col.append (str(i))

        df3 = pd.DataFrame (qws,columns= col)

        ax = df3.plot.bar(x= 'qtr',stacked= False, width=0.8,
                  title= country+" -"+title+" Quarters compared")
        plt.xlabel ('Quarters')
        plt.ylabel ('Total '+title)
        for container in ax.containers:
            ax.bar_label(container)
        #plt.tight_layout ()
        plt.show ()




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

#gen_bar (lb, 2018, 2022, 0, 'UK (England + Wales)', 0)


