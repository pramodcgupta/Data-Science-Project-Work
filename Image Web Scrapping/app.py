# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:22:47 2020

@author: Pramodkumar Gupta
"""

from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/showImages')
def displayImages():
    list_images=os.listdir('static')
    print(list_images)
    
    try: 
        if (len(list_images) > 1): 
            return render_template('showImages.html',user_images=list_images)
        else:
            return "Images are not present"
        
    except Exception as e:
        print("No images found",e)
        return "Please try with a different serach keyword"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 8000)
    #app.run(debug=True) # to run on cloud
