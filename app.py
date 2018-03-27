from __future__ import print_function
from flask import Flask, request
from flask_cors import CORS
import os
import unitTest as ut
import sys

app = Flask(__name__)
CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'upload_data'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ut.change_model(4, 3)


# @app.route('/model', methods=['POST'])
# def change_model():
#     return ut.change_model(int(request.form['model']), int(request.form['nb_class']))


@app.route('/upload', methods=['POST'])
def upload():
    # ut.test(request.form['file'])
    # return 'ajevfbezn'
    # image = request.files['file']
    # image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    # return ut.predict(image.filename)
    return ut.predict(request.form['file'])


if __name__ == '__main__':
    app.run(debug=True)
