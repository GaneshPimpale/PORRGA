# import packages: SolidPython
from solid import *
from solid.utils import *
from itertools import chain, combinations


class Resize:

    def __init__(self, scad_file):
        self.scad_file = scad_file
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
    def assign(self, param1, param2, param3):
        if self.scad_file == 'cone.scad':
            self.r1 = param1
            self.r2 = param2
            self.h = param3
        elif self.scad_file == 'cylinder.scad':
            self.r1 = param1
            self.r2 = param2
            self.h = param3
        elif self.scad_file == 'rectangularPrism.scad':
            self.h = param1
            self.l = param2
            self.w = param3
        else:
            self.r = param1
            self.h = param2

    # resize parameters
    def iterate(self):
        x = range(3, 20, 2)
        i = 1
        if self.scad_file == 'cone':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = self.scad_file.cylinder(param1, param2, param3)

        elif self.scad_file == 'cylinder':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = self.scad_file.cylinder(param1, param2, param3)

        elif self.scad_file == 'rectangularPrism.scad':
            list = intertools.combinations(x, 3)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                param3 = list[0:i:2]
                scad = self.scad_file.box(param1, param2, param3)

        else:
            list = intertools.combinations(x, 2)
            for i in range(0, len(list)):
                param1 = list[0:i:0]
                param2 = list[0:i:1]
                scad = self.scad_file.ellipse(param1, param2)

    def render_to_scadfile:
        scad_render_to_file(scad, 'example.scad')