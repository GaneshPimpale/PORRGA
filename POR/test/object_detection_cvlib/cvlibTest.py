import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

class cvlibTest:

    def object_detect(image):
        img = cv2.imread(image)
        bbox, label, conf = cv.detect_common_objects(img)
        output_image = draw_bbox(img, bbox, label, conf)
        plt.imshow(output_image)
        plt.show()

    object_detect('C:/Users/ehuan/Desktop/SHTEM/PORRGA/POR/testImages/TEST2.jpg')