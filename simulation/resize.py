# import packages: SolidPython
from solid import *
from solid.utils import *
from itertools import chain, combinations


class Resize:

    def __init__(self, scad_file):
        #self.scad_file = scad_file
        self.scad_file = import_scad(scad_file)
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
        if self.scad_file == 'cone.scad':
            tempList = list(combinations(x, 3))
            for i in range(0, 3):
                param1 = tempList[i][0]
                param2 = tempList[i][1]
                param3 = tempList[i][2]
                filepath = 'produced_scad_files/' + 'cone' + str(param1) + '_' + str(param2) + '_' + str(param3) + '.scad'
                scad_render_to_file(self.scad_file.cone(param1, param2, param3), filepath)

        elif self.scad_file == 'cylinder.scad':
            tempList = list(combinations(x, 3))
            for i in range(0, 3):
                param1 = tempList[i][0]
                param2 = tempList[i][1]
                param3 = tempList[i][2]
                filepath = 'produced_scad_files/' + 'cylinder' + str(param1) + '_' + str(param2) + '_' + str(param3) + '.scad'
                scad_render_to_file(self.scad_file.cylinder(param1, param2, param3), filepath)

        elif self.scad_file == 'rectangularPrism.scad':
            tempList = list(combinations(x, 3))
            for i in range(0, 3):
                param1 = tempList[i][0]
                param2 = tempList[i][1]
                param3 = tempList[i][2]
                filepath = 'produced_scad_files/' + 'rectangularPrism' + str(param1) + '_' + str(param2) + '_' + str(
                    param3) + '.scad'
                scad_render_to_file(self.scad_file.cylinder(param1, param2, param3), filepath)

        else:
            tempList = list(combinations(x, 2))
            for i in range(0, 2):
                param1 = tempList[i][0]
                param2 = tempList[i][1]
                filepath = 'produced_scad_files/' + 'ellipse' + str(param1) + '_' + str(param2) + '_' + '.scad'
                scad_render_to_file(self.scad_file.ellipse(param1, param2), filepath)

    def render_to_scadfile(self):
        scad_render_to_file(scad, 'example.scad')