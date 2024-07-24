from flask import Flask,request
import joblib
import json
import numpy as np

model = joblib.load('/home/karam/Projects/AI/Personal/fpl/deployment/static/model.lgbm')
app = Flask(__name__)

@app.route('/',methods=['POST'])
def predict():
    print(request.data)
    data = np.array(json.loads(request.data.decode())['X']).reshape(1,-1)
    pd = list(model.predict(data))
    return {'prediction':list(pd)}
app.run()