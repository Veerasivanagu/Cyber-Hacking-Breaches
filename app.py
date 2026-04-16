#importing required libraries

from flask import Flask, request, render_template,redirect
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import re
import pymsgbox

import pickle
warnings.filterwarnings('ignore')


pickle_in = open('model.pkl','rb')
pac = pickle.load(pickle_in)
tfid = open('tfidf_vectorizer.pkl','rb')
tfidf_vectorizer = pickle.load(tfid)


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/performance')
def performance():
	return render_template('performance.html')

@app.route('/chart')
def chart():
	return render_template('chart.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')



@app.route("/charts", methods=["GET", "POST"])
def charts():
   #if request.method == 'POST':    
         
       #query_content=request.form['news']
       #news=['query_content']
       #msg = '' 
       abc = request.args.get('news')
       
       #input_data=re.search("(?P<url>https?://[^\s]+)",abc).group("url")
       #string = [input_data.rstrip()]
       pattern =  r'(?:http://)?\w+\.\S*[^.\s]'
       input_data=re.findall(pattern, abc)
	    
       if input_data:
           
 
         tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
        
         y_pred = pac.predict(tfidf_test)
	#if y_pred[0] == 'bad':
	 #  label="malware"
	#elif y_pred[0] == 'good':
	 #  label="no malware"
         pred=format(y_pred[0])
         for x in input_data:
            return render_template('prediction.html', preds=pred, url=x)
       else :
        pymsgbox.alert('Enter the url', 'warning')
        return render_template('prediction.html')
           
    #    return redirect('/prediction') 
        


if __name__ == "__main__":
    app.run(debug=True)