# import packages: SolidPython
from solid import *
from solid.utils import *
from random import randint


class Resize:

    def __init__(self, ):
        # cone/cylinder parameters
        self.r1 = 0
        self.r2 = 0
        self.h = 0
        # rectangular prism parameters (height declared above)
        self.w = 0
        self.l = 0
        # ellipse parameters (height declared above)
        self.r = 0

    # import OpenScad code (file name corresponds to shape)
    scad_file = import_scad('/path/to/example.scad')

    # classify shape + parameters
    def assign(self, scad_file, param1, param2, param3):
        if scad_file == 'cone.scad':
            self.param1 = r1
            self.param2 = r2
            self.param3 = h
        elif scad_file == 'cylinder.scad':
            self.param1 = r1
            self.param2 = r2
            self.param3 = h
        elif scad_file == 'rectangularPrism.scad':
            self.param1 = h
            self.param2 = l
            self.param3 = w
        else:
            self.param1 = r
            self.param2 = h

    # resize parameters
    def inrate(self):
        if scad_file == 'cone':
            intertools.combinations(range(11), 3)
            # need to set param values
        elif scad_file == 'cylinder':
            intertools.combinations(range(11), 3)

        elif scad_file == 'rectangularPrism.scad':
            intertools.combinations(range(11), 3)

        else:
            intertools.combinations(range(11), 2)

    # render to file (STL/scad)
    scad_render_to_file(scad, 'example.scad')