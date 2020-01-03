
"""
import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
import random
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATADIR = 
CLASSES = 
BATCH_SIZE = 32
IMG_SIZE = 50
IMG_SIZE = 50

train_data = []
test_data = []
X = y = []


def prep_training_data():
    for category in CLASSES:
        path = os.path.join(DATADIR, category)
        class_num = CLASSES.index(category)
        for image in os.listdir(path):
            try:
                image_arr = cv2.imread(os.path.join(
                    path, image), cv2.IMREAD_GRAYSCALE)
                n_arr = cv2.resize(image_arr, (IMG_SIZE, IMG_SIZE))
                train_data.append([n_arr, class_num])
            except Exception as e:
                pass


# def prep_test_data():


prep_training_data()
random.shuffle(train_data)
for features, labels in train_data:
    X.append(features)
    y.append(labels)

try:
    pickle_out = open("X.pickle", "wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()
except Exception as e:
    print(f"Something went wrong : {e}")
"""
