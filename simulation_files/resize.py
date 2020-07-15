# import packages: SolidPython
from solid import *
from solid.utils import *
from itertools import chain, combinations


class Resize:

    def __init__(self, ):
        # cone/cylinder param:
        self.r1 = 0
        self.r2 = 0
        self.h = 0
        # rectangular prism param:
        self.w = 0
        self.l = 0
        # ellipse param:
        self.r = 0

    # import OpenScad code (file name corresponds to shape)
    scad_file = import_scad('/path/to/example.scad')

    # classify shape + parameters
    def assign(self, scad_file, param1, param2, param3):
        if scad_file == 'cone.scad':
            self.r1 = self.param1
            self.r2 = self.param2
            self.h = self.param3
        elif scad_file == 'cylinder.scad':
            self.r1 = self.param1
            self.r2 = self.param2
            self.h = self.param3
        elif scad_file == 'rectangularPrism.scad':
            self.h = self.param1
            self.l = self.param2
            self.w = self.param3
        else:
            self.r = self.param1
            self.h = self.param2

    # resize parameters
    def iterate(self):
        x = range(3, 20, 2)
        i = 1
        if scad_file == 'cone':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = scad_file.cylinder(param1, param2, param3)

        elif scad_file == 'cylinder':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = scad_file.cylinder(param1, param2, param3)

        elif scad_file == 'rectangularPrism.scad':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = scad_file.box(param1, param2, param3)

        else:
            list = intertools.combinations(x, 2)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                scad = scad_file.ellipse(param1, param2)

    def render_to_scadfile:
        scad_render_to_file(scad, 'example.scad')