from flask import Flask, request, jsonify, render_template, url_for
import joblib
import numpy as np

model = joblib.load('/workspaces/fantasy-predictions/deployment/static/model.lgbm')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = [float(request.form[key]) for key in request.form]
        num_features_model = 21  
        num_features_input = len(data) 
        if num_features_input < num_features_model:
            data.extend([0] * (num_features_model - num_features_input))
        np_data = np.array(data).reshape(1, -1)
        output = model.predict(np_data)
        return jsonify({'prediction': output.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)