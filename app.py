from __future__ import print_function
from flask import Flask, request
import os
import unitTest as ut

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'upload_data'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/model', methods=['POST'])
def change_model():
    return ut.change_model(int(request.form['model']), int(request.form['nb_class']))


@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['']
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    return ut.predict(image.filename)


if __name__ == '__main__':
    app.run(debug=True)
