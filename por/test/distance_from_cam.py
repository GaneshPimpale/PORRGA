import cv2
import numpy as np
from matplotlib import pyplot

# Initiate camera:
cap = cv2.VideoCapture()



# Loop:
while (cv2.waitKey(20) & 0xFF != ord("q")):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
cv2.destroyAllWindows()