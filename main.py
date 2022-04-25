#importing the library
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

#load the model
model = joblib.load("model\social_networks_ads.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data',methods=['post'])
def data():
    age = request.form.get('Age')
    salary = request.form.get('Salary')

    result = model.predict([[age,salary]])

    if result==0:
        data = "Person will buy it"
    else:
        data = "Person will not buy it"

    print(data)

    return render_template('predict.html', data = data)

app.run(debug= True)
