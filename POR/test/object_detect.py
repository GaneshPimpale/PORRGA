import imutils
from imutils.video import VideoStream
from imutils.video import FPS

import numpy as np
import cv2

import time
import argparse


# Argument parse
parser = argparse.ArgumentParser()
parser.add_argument("--video")
parser.add_argument("--prototxt", default="MobileNetSSD_deploy.prototxt")
parser.add_argument("--model", default="MobileNetSSD_deploy.caffemodel")
parser.add_argument("--confidence", default=0.2, type=float)
args = vars(parser.parse_args())

# Initialize classes list and generate bounding box colors
CLASSES = ["background", "person", "phone"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES)))

# Load model
network = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# Start video stream and FPS counter
vs = VideoStream(src=0).start()
fps = FPS().start()

# Main loop
while cv2.waitKey(1) & 0xFF != ord("q"):
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007834, (300, 300), 127.5)

    network.setInput(blob)
    detections = network.forward()

    for i in np.arange(0, detections.shape[2]):
        confid = detections[0, 0, 1, 2]
        if confid > args["confidence"]:
            # Find X, Y coordinates of the detections
            index = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Add the prediction on the frame
            label = CLASSES[index] + ": " + str(confid*100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[index], 2)
            y = startY-15 if startY-15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[index], 2)

    # Show output and update FPS
    cv2.imshow("Cam", frame)
    fps.update()

# Stop all
fps.stop()
cv2.destroyAllWindows()
vs.stop()

