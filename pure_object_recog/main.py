import os
import shutil
import sys

from pyodm import Node
import cv2

from pure_object_recog.pure_object import Por
from pure_object_recog.parameter import Popr



por = Por()
# Collect photo data
# TODO: make sure cam_list is up to date
cam_list = [0, 1, 2, 3]
por.camera_input(cam_list)

# Create node connection
nd = Node("localhost", 3000)
por.create_mesh(nd)




