# Air Quality Index Project

'''
Author: Pramodkumar Gupta
1. Data Collection 
Website: https://en.tutiempo.net/
Script: Html_script.py
'''

'''
Step 1: Data Collection from Webpage
'''
import os
import sys
import time
import requests


def retrieve_html(): 
    
    for year in range(2013,2019): 
        for month in range(1,13): 
            if month < 10: 
                url="https://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month,year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month,year)
            
            url_data=requests.get(url)
            url_txt=url_data.text.encode('utf-8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)): 
                os.makedirs("Data/Html_Data/{}".format(year))
            
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output: 
                output.write(url_txt)
                
    sys.stdout.flush
                

if __name__ == "__main__": 
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time Taken: {}".format(stop_time - start_time))
    