from flask import Flask,request, jsonify, render_template
import joblib
import json
import numpy as np

model = joblib.load('/workspaces/fantasy-predictions/deployment/static/model.lgbm')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print(request.data)
    data = np.array(json.loads(request.data.decode())['X']).reshape(1,-1)
    pd = list(model.predict(data))
    return {'prediction':list(pd)}
app.run(debug=True)