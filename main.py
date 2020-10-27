import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from joblib import dump, load

app = Flask(__name__)  # Initialize the flask App'))

# open our vectorizer and model with joblib
nmf = load('models/nmf_tf_idf_model')
vectorizer = load('models/tf_idf')
#topics = ['Job Monitoring', 'Account Issues', 'Outage Problems', 'Ticket Management', 'Application Access']

topics = ['Job Monitoring', 'Change Request', 'Account Issues', 'Outage Problems',  'Application Access']

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    issue_description = request.form['description']    
    text_vect = vectorizer.transform([issue_description])
    result = nmf.transform(text_vect)
    output = topics[np.argmax(result)]

    return render_template('index.html', prediction_text='"{}"'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
