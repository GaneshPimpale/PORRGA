import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

class cvlib_real_time_object_detection:

    def __init__(self):
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print('could not open webcam')
            exit()
        while cam.isOpened():
            ret, frame = cam.read()
            if not ret:
                break
            bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25)
            print(bbox, label, conf)
            output = draw_bbox(frame, bbox, label, conf)
            cv2.imshow('Real Time Object Detection', output)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()
test = cvlib_real_time_object_detection()