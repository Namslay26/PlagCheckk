import os
from flask import *
from flask import render_template
from difflib import SequenceMatcher

app = Flask(__name__)
app.config["FILE_UPLOADS"]="\vsneh\Plagcheck_website\files"

#mainpage
@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/query')
def query():
    print(request.query_string)
    return "no query recieved",400

#upload file
@app.route('/upload',methods=['POST','GET'])
def upload():

    if request.method=="POST":
        if request.files and len(request.files) > 1:
            similarity = SequenceMatcher(None, request.files['text1'].read().decode('utf-8'), request.files['text2'].read().decode('utf-8')). ratio() 
            percent = similarity*100
            return render_template('result.htm',result=percent)
        

if __name__=='__main__':
    app.run(debug=True)