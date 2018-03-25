from __future__ import print_function
import sys
import cv2
import numpy as np
import os
from os.path import isfile, join
import settings

globalLabels = []

def loadImage(filePath):
    image = cv2.imread(filePath)
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image


def resize_image(fileName, final_height, final_width):
    image = loadImage('upload_data/' + fileName)
    height, width, channels = image.shape
    final_ratio = float(final_width) / final_height
    ratio = float(width / height)
    if ratio < final_ratio:
        wanted_width = round(final_ratio * height)
        border = int(wanted_width - width)
        blank_image = np.zeros((height, border, 3), np.uint8)
        blank_image[:, :] = (255, 255, 255)
        final = np.concatenate((image, blank_image), axis=1)
    elif ratio > final_ratio:
        wanted_height = round(width / final_ratio)
        border = int(wanted_height - height)
        blank_image = np.zeros((border, width, 3), np.uint8)
        blank_image[:, :] = (255, 255, 255)
        final = np.concatenate((image, blank_image), axis=0)
    else:
        final = image
    resized_image = cv2.resize(final, (final_width, final_height))
    if not os.path.isdir('processed_data'):
        os.makedirs('processed_data')
    return cv2.imwrite('processed_data/' + fileName.split('.')[0] + '.jpg', resized_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])