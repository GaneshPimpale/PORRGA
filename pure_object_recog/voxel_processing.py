import os
import shutil
import sys

import numpy as np
import matplotlib.pyplot as plt

from pyntcloud import PyntCloud
import binvox


class Voxel:

    def __init__(self):
        self.voxel_file_path = "temp"

    def get_voxel(self, path):
        self.voxel_file_path = path

    def find_curve(self):
        return -1

   def display_voxel(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')



