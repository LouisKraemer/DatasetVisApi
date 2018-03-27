from __future__ import print_function
from StringIO import StringIO
from PIL import Image
import base64
import cv2
import sys
import settings
import numpy as np
import loadData as ld
import reseau as re
import json

global_model = None

label_array = []

size = None


def change_model(index, nb_class):
    global global_model
    global label_array
    global size
    global_model = None
    global_model = re.getReseau(index, nb_class)
    global_model.load("models/" + str(index) + "_" + str(nb_class) + "/dataviz-classifier.tfl")
    data = json.load(open("models/" + str(index) + "_" + str(nb_class) + "/result.json"))
    size = data['settings']['size']
    label_array = []
    for prediction in data['results'][0]['predictions']:
        label_array.append(prediction['label'])
    return 'success'


def predict(base64_file):
    if global_model is None:
        return 'error'

    image = ld.resize_image(base64_file, size, size)

    # print(image, file=sys.stdout)
    result = {
        'predictions': []
    }

    predictions = global_model.predict([image])

    for i, label in enumerate(label_array):
        result['predictions'].append({
            'label': label,
            'proba': predictions[0][i].item()
        })

    return json.dumps(result)
