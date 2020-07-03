#Tensorflow/Keras Libraries:
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.ResNet152V2 import ResNet152V2, preprocess_input, decode_predictions

#Other Libraries:
import numpy as np
import cv2


def identification(image):
    model = ResNet152V2()
    img = load_img(image, target_size = (224, 224))
    img = img_to_array(img)
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
    img = preprocess_input(img)
    yhat = model.predict(img)
    tag = decode_predictions(yhat)
    tag = tag[0][0]
    print(tag[1])
    print(tag[2]*100)

identification("/home/ganesh/workspaces/PORRRGA/POR/testImages/Test3.jpg")

