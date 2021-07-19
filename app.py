# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:06:02 2021

@author: Pureti
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('visibility_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    input_features = [float(x) for x in request.form.values()]
    input_features = [np.array(input_features)]
    prediction = model.predict(input_features)

    prediction = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Visibility for the given weather data : {prediction} km')

"""if __name__ == "__main__":
    app.run(debug=True)"""