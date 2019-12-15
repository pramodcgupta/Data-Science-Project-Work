# -*- coding: utf-8 -*-
"""
Author: Pramodkumar Gupta
Script: Extract_combine.py
"""

# Import All libraries
from Plot_AQI import avg_data
import requests
import sys
import os
from bs4 import BeautifulSoup
import csv
import pandas as pd

def met_data(month, year): 
    
    file_html=open("Data/Html_Data/{}/{}.html".format(year,month),"rb")
    plain_text=file_html.read()
    
    tempD=[]
    finalD=[]
    
    soup=BeautifulSoup(plain_text,"lxml")
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}): 
        for tbody in table: 
            for tr in tbody: 
                a=tr.get_text()
                tempD.append(a)
    
    rows = len(tempD)/15
    
    for times in range(round(rows)): 
        tempnewD=[]
        
        for i in range(15): 
            tempnewD.append(tempD[0])
            tempD.pop(0)
            
        finalD.append(tempnewD)         
        
    finalD.pop(len(finalD) -1) # Remove last row
    finalD.pop(0)   # Remove first row which contain Headers
    
    for a in range(len(finalD)): 
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
    
    return finalD     

def CSVtoDataFrame(filename): 
    return pd.read_csv(filename)

if __name__ == "__main__": 
    
    if not os.path.exists("Data/Real-Data"): 
            os.makedirs("Data/Real-Data")
            
    for year in range(2013,2017):         
        yeardata=[]
        
        for month in range(1,13): 
            finalD=met_data(month,year)
            yeardata=yeardata + finalD
            
        # Get Depedent Feature
        lst= avg_data('Data/AQI/aqi{}.csv'.format(year))
        
        # Combine Depedent and Independent Features
        for element in range(len(yeardata)-1): 
            yeardata[element].insert(8,lst[element])
            
        with open("Data/Real-Data/real_{}.csv".format(year),"w") as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            
            for row in yeardata: 
                flag = 0
                for element in row: 
                    if element in ('','-'): 
                        flag=1                
                if flag == 0: 
                    wr.writerow(row)
     
        
    data2013=CSVtoDataFrame('Data/Real-Data/real_2013.csv')
    data2014=CSVtoDataFrame('Data/Real-Data/real_2014.csv')                            
    data2015=CSVtoDataFrame('Data/Real-Data/real_2015.csv')
    data2016=CSVtoDataFrame('Data/Real-Data/real_2016.csv')     

    total = pd.concat([data2013,data2014,data2015,data2016],axis=0)
    
    total.to_csv('Data/Real-Data/real_Combine.csv',index=False)
    
    
       
            
            
            
            
    
    
    