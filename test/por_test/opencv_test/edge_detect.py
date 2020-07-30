import cv2
import numpy as np
from matplotlib import pyplot
import pandas as pd
import scipy
import peakutils

# Input file:
img = cv2.imread("/home/ganesh/workspaces/PORRGA/POR/testImages/TEST10.jpg")

# Grayscale Image:    #Do I even need this???
grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# HSV Image:    #Do I even need this???
HSVImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Blur Image:
blurX = 10
blurY = 10
blurImg = cv2.blur(img, (blurX, blurY))

# Posterize/quantize image:
n = 2  # quantization level

###   ALL OF THIS STUFF IS NOT FINAL!!!
indices = np.arange(0, 256)  # List of all colors
divider = np.linspace(0, 255, n + 1)[1]  # we get a divider
quantiz = np.int0(np.linspace(0, 255, n))  # we get quantization colors
color_levels = np.clip(np.int0(indices / divider), 0, n - 1)  # color levels 0,1,2..
palette = quantiz[color_levels]  # Creating the palette

pImg = palette[blurImg]  # Applying palette on image
pImg = cv2.convertScaleAbs(pImg)  # Converting image back to uint8
###


# Edge detection:
lowerColor = np.array([30, 150, 50])
upperColor = np.array([255, 255, 180])

mask = cv2.inRange(img, lowerColor, upperColor)
edge = cv2.Canny(img, 100, 200)

maskQ = cv2.inRange(pImg, lowerColor, upperColor)
edgeQ = cv2.Canny(pImg, 100, 200)

# Resizing and Formatting:
scale = 100
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dimensions = (width, height)

resizeImg = cv2.resize(img, dimensions)
resizeBImg = cv2.resize(blurImg, dimensions)
resizeEImg = cv2.resize(edge, dimensions)

resizePImg = cv2.resize(pImg, dimensions)
resizeEQImg = cv2.resize(edgeQ, dimensions)

"""
#Histogram analysis:
color = ("r", "g","b")
for i, col in enumerate(color):
    X = cv2.calcHist([pImg], [i], None, [256], [0, 256])
    indexes = peakutils.indexes(Y, thres=0.5, min_dist=30)
    print(indexes)
    pyplot.plot(X, color = col)
#Threshold based deconstruction:
"""

# Output:
# finalImg =  cv2.addWeighted(resizePImg, 0.5, resizeEImg, 0.5, 0)

while (cv2.waitKey(20) & 0xFF != ord("q")):
    # Show images
    cv2.imshow("TEST Original", resizeImg)
    cv2.imshow("TEST Blur", resizeBImg)
    cv2.imshow("TEST Quantization", resizePImg)
    cv2.imshow("TEST Plain Edge", resizeEImg)
    cv2.imshow("TEST Edge on Quantization", resizeEQImg)
    # cv2.imshow("TEST Quantization & Edge", finalImg)

    pyplot.show()

cv2.destroyAllWindows()