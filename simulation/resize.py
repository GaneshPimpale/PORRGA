# import packages: SolidPython
from solid import *
from solid.utils import *
from itertools import chain, combinations, permutations


class Resize:

    def __init__(self, scad_file, target_range):
        self.scad_file = scad_file
        #self.scad_file = import_scad(scad_file)
        # cone/cylinder param:
        self.r1 = 0
        self.r2 = 0
        self.h = 0
        # rectangular prism param:
        self.w = 0
        self.l = 0
        # ellipse param:
        self.r = 0

        self.target_range = target_range
        self.list_two = list(permutations(self.target_range, 2))
        self.list_three = list(permutations(self.target_range, 3))
        self.list_four = list(permutations(self.target_range, 4))
        self.counter = 0
        self.total_len = len(self.list_two) + len(self.list_three) + len(self.list_four)


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
        if self.scad_file == 'cone.scad':
            current_permutation = self.list_two[self.counter]
            scad_render_to_file(cylinder(h=current_permutation[0], r1=current_permutation[1], r2=0), 'current_stl.stl')
            self.counter+=1
        elif self.scad_file == 'cylinder.scad':
            current_permutation = self.list_two[self.counter]
            scad_render_to_file(cylinder(h=current_permutation[0], r1=current_permutation[1], r2=current_permutation[1]), 'current_stl.stl')
            self.counter += 1
        elif self.scad_file == 'rectangularPrism.scad':
            current_permutation = self.list_three[self.counter]
            scad_render_to_file(cube(size=(current_permutation[0], current_permutation[1], current_permutation[2])), 'current_stl.stl')
            self.counter += 1
        elif self.scad_file == 'ellipse.scad':
            current_permutation = self.list_three[self.counter]
            scad_render_to_file(scale([current_permutation[0], current_permutation[1], current_permutation[2]])(sphere(r=current_permutation[3])), 'current_stl.stl')
            self.counter += 1