# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/classes")
def classes():
    return '''My classes for next semester are:
            Advanced Programming 
            Discrete Maths
            Intermediate Macroeconomics 
            Contemporary Civilizations
            Art and Musics of Southern India
            '''
            
@app.route("/biggestinspirations")
def classes123():
    return '''My biggest inspirations is Gordon Ramsay'''



#start the server
if __name__ == "__main__":
    app.run()