import os
import cv2
import numpy as np
from pyntcloud import PyntCloud
from pyodm import Node


class Por:

    def __init__(self):
        self.image_list = []
        self.mesh_file

    """ Get pic from each camera in list
    :param cam_list: list of camera input ints
    """
    def camera_input(self, cam_list, img_path):
        for cam in cam_list:
            # get image from cam
            vid = cv2.VideoCapture(cam)
            if not vid.isOpened():
                raise Exception("cam #" + str(cam) + " cannot be opened")
            ret, frame = vid.read()

            # create image path
            img_name = "cam_" + str(cam) + "_pic.png"
            path = img_path + img_name

            # add path to list and write to disk
            self.image_list.append(path)
            cv2.imwrite(path, frame)
            print("cam #" + str(cam) + " read")

    """ Uses PyODM to generate a 3D mesh from multiple images 
    :param node_connection: Node connection to the ODM server
    :param result_location: File location of the 
    """
    def create_mesh(self, node_connection):
        print("creating ODM task")
        task = node_connection.create_task(self.image_list, )
        task.wait_for_completion()
        # TODO: decide on file location
        os.listdir(task.download_assets(""))

    """ Turns mesh into voxel numpy array """
    def voxelize(self, ):
        return -1

    """ Classify voxel group """
    def classify(self):
        return -1

    """ Perform initial position based segmentation """
    def pre_segment_voxel(self):
        return -1






