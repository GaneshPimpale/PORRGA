import os
import shutil
import sys

import numpy as np
import matplotlib.pyplot as plt

from pyntcloud import PyntCloud
import pyvista as pv
import binvox


class Voxel:

    def __init__(self):
        self.voxel_file_path = "temp"

    """ Get pic from each camera in list
    :param path: Path to .ply file
    """
    def get_voxel(self, path):
        self.voxel_file_path = path
        mesh = pv.read(self.voxel_file_path)

    """ Crate array storing each voxel's relative position per dimension """
    def create_voxel_array(self):
        return -1

    """ Finds the lines in the voxels parallel to the dimension vectors 
    
    For each voxel in the voxel mesh create a relation array in the format of [X, Y ,Z]
    
    """
    def find_lines(self):
        return -1

    """ Find the rectangles given two dimensions 
    
    Define the Taylor Series created by the differences in length between dimension lines on a single 
    plane. Use the approximated function to find straight edges.
    
    :param :
    """
    def find_rect(self):
        return -1

    """ Find the elipses given two dimensions 
    
    Define the Taylor Series created by the differences in length between dimension lines on a single 
    plane. Use the approximated function to find curves edges.
    
    :param :
    """
    def find_elipse(self):
        return -1

    """ Find stacks of 2D shapes in all dimensions 
    
    Depending on the orientation of the stacks, in each orientation, classify the shapes into 
    one of 4 pure object types.
    
    :param :
    """
    def find_shapes(self):
        return -1

    """ Find over-classified shapes and reclassify them 
    
    If a part of the voxel shape has been classified in multiple dimensions separate these 
    sections from the rest of the classifies shape and reclassify these parts
    
    :param : 
    """
    def segment_over_classified_shapes(self):
        return -1

    def display_voxel(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')



