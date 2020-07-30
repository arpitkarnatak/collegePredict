from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Pickle.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

##'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
     ##  'LOR', 'CGPA', 'Research'

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        GRE = int(request.form['GRE Score'])
        TOEFL = int(request.form['TOEFL Score'])
        UnivRank = int(request.form['University Rating'])
        SOP = int(request.form['SOP'])
        LOR = int(request.form['LOR '])
        CGPA = float(request.form['CGPA'])
        Res=request.form['Research']
        if(Res=='Yes'):
            Res=1
        else:
            Res=0
        prediction=model.predict([[GRE,TOEFL,UnivRank,SOP,LOR,CGPA,Res]])
        output=prediction*100
        return render_template('index.html',prediction_text="Your odds of getting a college for Masters is {}%".format(output))

if __name__=="__main__":
    app.run(debug=True)