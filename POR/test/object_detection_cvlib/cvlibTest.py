import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

class cvlibTest:

    def object_detect(image):
        #read in image
        img = cv2.imread(image)
        #convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #detect objects
        bbox, label, conf = cv.detect_common_objects(img)
        #display labels
        output_image = draw_bbox(img, bbox, label, conf)
        #display output image
        plt.imshow(output_image)
        plt.show()

    object_detect('C:/Users/ehuan/Desktop/SHTEM/PORRGA/POR/testImages/TEST2.jpg')