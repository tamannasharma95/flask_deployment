import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/world', methods=['POST'])
def world():
    import pdb 
    pdb.set_trace() 
    return 'World'

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)