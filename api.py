from flask import Flask, request, render_template, url_for, redirect, flash
from markupsafe import escape
import numpy as np
import pickle
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# LOAD THE MODEL HERE
# model = pickle.load(open())


@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == "POST":
        text = request.form.get("title")
        return redirect("output")
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [np.array(data['data'])]
    prediction = model.predict(features)
    return str(prediction[0])

@app.route('/output')
def output():
    return render_template('output.html')


if __name__ == "__main__":
    app.run(debug=True)