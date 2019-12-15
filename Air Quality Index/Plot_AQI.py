# -*- coding: utf-8 -*-
'''
Author: Pramodkumar Gupta
Data Cleaning
https://en.tutiempo.net/
Script: Plot_AQI.py
'''

import pandas as pd
import matplotlib.pyplot as plt

def avg_data(filename): 
    
    'This function defines average all data daily'       
    average=[]
    
    for rows in pd.read_csv(filename, chunksize=24): 
       
        var=0.0
        avg=0.0
        data = []       
        for index, row in rows.iterrows(): 
            data.append(row['PM2.5'])
            
        for num in data:                            
            if type(num) is float or type(num) is int:     
                var=var+num
            elif type(num) is str and num not in ['NoData', 'PwrFail', '---' , 'InVld']:    
                var=var+float(num)
        
        avg=var/24
               
        average.append(avg)
     
    return average               
            


if __name__ == "__main__": 
    
    # Call function for year 2013 to 2018
    
    lst2013= avg_data('Data/AQI/aqi2013.csv')
    lst2014= avg_data('Data/AQI/aqi2014.csv')
    lst2015= avg_data('Data/AQI/aqi2015.csv')
    lst2016= avg_data('Data/AQI/aqi2016.csv')
    lst2017= avg_data('Data/AQI/aqi2017.csv')
    lst2018= avg_data('Data/AQI/aqi2018.csv')
    
    # Visualize data
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.plot(range(0,365),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
    