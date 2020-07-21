import os
import shutil
import sys

import cv2
import numpy as np

from pyntcloud import PyntCloud
from pyodm import Node


class Por:

    def __init__(self):
        # Create global variables
        self.temp_path = os.path.realpath("temp") + "/run"
        self.image_list = []
        self.mesh_file

        # Create temp file directory
        self.image_path = self.temp_path + "/images"
        self.odm_path = self.temp_path + "/odm_results"

    """ Get pic from each camera in list
    :param cam_list: list of camera input ints
    """
    def camera_input(self, cam_list):
        for cam in cam_list:
            # Get image from cam
            vid = cv2.VideoCapture(cam)
            if not vid.isOpened():
                raise Exception("cam #" + str(cam) + " cannot be opened")
            ret, frame = vid.read()

            # Create image path
            img_name = "cam_" + str(cam) + "_pic.png"
            path = self.image_path + img_name

            # Add path to list and write to disk
            self.image_list.append(path)
            cv2.imwrite(path, frame)
            print("cam #" + str(cam) + " read")

    """ Directly write to the image list
    :param img_list: list of image paths
    """
    def write_to_image_list(self, img_list):
        self.image_list = img_list
        print("Wrote images to list")

    """ Uses PyODM to generate a 3D mesh from multiple images 
    :param node_connection: Node connection to the ODM server
    """
    def create_mesh(self, node_connection):
        print("Creating ODM task")
        task = node_connection.create_task(self.image_list, )
        print("Running task")
        task.wait_for_completion()
        os.listdir(task.download_assets(self.odm_path))

    """ Turns mesh into voxel numpy array """
    def voxelize(self, ):
        return -1

    """ Classify voxel group """
    def classify(self):
        return -1

    """ Perform initial position based segmentation """
    def pre_segment_voxel(self):
        return -1

    """ Will clean the temp file """
    def clean(self):
        shutil.rmtree(self.temp_path)






