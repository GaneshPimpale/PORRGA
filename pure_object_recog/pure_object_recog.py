import os
import cv2
import numpy as np
from pyntcloud import PyntCloud
from pyodm import Node


class Por:

    """ Get input values and files
    :param image_list: list of image files
    """
    def __init__(self, image_folders):
        self.image_list = image_folders

    """ Uses PyODM to generate a 3D mesh from multiple images """
    def create_mesh(self):
        nd = Node("localhost", 3000)
        nd.create_task(self.image_list, )

    """ Turns mesh into voxels """
    def voxelize(self, ):
        return -1

    """ Classify voxel group """
    def classify(self):
        return -1

    """ Perform initial position based segmentation """
    def pre_segment_voxel(self):
        return -1






