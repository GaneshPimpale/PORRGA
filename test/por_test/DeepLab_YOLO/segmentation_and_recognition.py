import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

from model import Deeplabv3

# Uses Keras implementation of Deeplabv3+ from https://github.com/bonlime/keras-deeplab-v3-plus
# To use this code, clone the above repository and run this code inside of it

# Uses cvlib to use YOLOv3 to detect and recognize objects in the image

# Generates Deeplab labels using most basic setup.  Supports various image sizes.  Returns image labels in same format
# as original image.  Normalization matches MobileNetV2
class Deeplab_YOLO:
    def segment_and_recognize(input):
        trained_image_width=512
        mean_subtraction_value=127.5
        image = np.array(Image.open(input))

        # get the YOLOv3 bounding boxes, labels and confidences
        bbox, YOLO_label, conf = cv.detect_common_objects(image)

        # resize to max dimension of images from training dataset
        w, h, _ = image.shape
        ratio = float(trained_image_width) / np.max([w, h])
        resized_image = np.array(Image.fromarray(image.astype('uint8')).resize((int(ratio * h), int(ratio * w))))

        # apply normalization for trained dataset images
        resized_image = (resized_image / mean_subtraction_value) - 1.

        # pad array to square image to match training images
        pad_x = int(trained_image_width - resized_image.shape[0])
        pad_y = int(trained_image_width - resized_image.shape[1])
        resized_image = np.pad(resized_image, ((0, pad_x), (0, pad_y), (0, 0)), mode='constant')

        # make prediction for Deeplab
        deeplab_model = Deeplabv3()
        res = deeplab_model.predict(np.expand_dims(resized_image, 0))
        labels = np.argmax(res.squeeze(), -1)

        # remove padding and resize back to original image
        if pad_x > 0:
            labels = labels[:-pad_x]
        if pad_y > 0:
            labels = labels[:, :-pad_y]
        labels = Image.fromarray(labels.astype('uint8')).resize((h, w)).convert()

        # converts PIL greyscale image to numpy array compatible with cvlib
        # and overlays the segment over original input image
        temp = 'temp.png'
        plt.imsave(temp, labels)
        background = Image.open(input).convert('RGBA')
        segments = Image.open(temp)
        overlay = Image.blend(background, segments, 0.5)
        img = np.array(overlay)

        # display the YOLOv3 bounding boxes and labels on the overlay
        img = draw_bbox(img=img, bbox=bbox, labels=YOLO_label, confidence=conf)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        os.remove(temp)

        # show final result
        plt.imshow(img)
        plt.waitforbuttonpress()
        plt.show()

test = Deeplab_YOLO.segment_and_recognize('test.jpg')
