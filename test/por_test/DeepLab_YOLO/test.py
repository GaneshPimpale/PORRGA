import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

from model import Deeplabv3

# Generates labels using most basic setup.  Supports various image sizes.  Returns image labels in same format
# as original image.  Normalization matches MobileNetV2

trained_image_width=512
mean_subtraction_value=127.5
image = np.array(Image.open('test.jpg'))

#get the YOLOv3 bounding boxes, labels and confidences
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

# make prediction
deeplab_model = Deeplabv3()
res = deeplab_model.predict(np.expand_dims(resized_image, 0))
labels = np.argmax(res.squeeze(), -1)

# remove padding and resize back to original image
if pad_x > 0:
    labels = labels[:-pad_x]
if pad_y > 0:
    labels = labels[:, :-pad_y]
labels = Image.fromarray(labels.astype('uint8')).resize((h, w)).convert()




#this is a really stupid way to get the PIL image to work with OpenCV but it works
plt.imsave('./temp_image_this_is_so_dumb.png', labels)
background = Image.open('test.jpg').convert('RGBA')
segments = Image.open('temp_image_this_is_so_dumb.png')
overlay = Image.blend(background, segments, 0.5)
img = np.array(overlay)
#img = cv2.imread('temp_image_this_is_so_dumb.png')
#display the YOLOv3 bounding boxes and labels
img = draw_bbox(img=img, bbox=bbox, labels=YOLO_label, confidence=conf)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)

plt.waitforbuttonpress()
plt.show()
os.remove('temp_image_this_is_so_dumb.png')
