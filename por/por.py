import os
import cv2
import numpy as np
from pyntcloud import PyntCloud
from pyodm import Node


class Por:

    """ Get input values and files
    :param image_list: list of image files
    """
    def __init__(self, image_list):
        self.image_list = image_list

    """ Uses PyODM to generate a 3D mesh from multiple images """
    def create_mesh(self):
        return -1

    """ Turns mesh into voxels """
    def voxelize(self, ):
        return -1

    """ Classify voxel group """
    def classify(self):
        return -1

    """ Perform initial position based segmentation """
    def pre_segment_voxel(self):
        return -1






