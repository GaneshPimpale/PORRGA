# import packages: SolidPython
from solid import *
from solid.utils import *
from itertools import chain, combinations, permutations
import pybullet as p


class Resize:

    def __init__(self, target_range):
        #self.scad_file = scad_file
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
        #self.total_len = len(self.list_two) + len(self.list_two) + len(self.list_three) + len(self.list_four)
        self.len_1 = len(self.list_two)
        self.len_2 = len(self.list_two) + len(self.list_two)
        self.len_3 = self.len_2 + len(self.list_three)
        self.len_4 = self.len_3 + len(self.list_four)





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
        filePath = 'Hand-Assem-By-Part-URDF.SLDASM/meshes/Example Sphere.STL'
        if self.counter < self.len_1:
            current_permutation = self.list_two[self.counter]
            scad_render_to_file(cylinder(h=current_permutation[0], r1=current_permutation[1], r2=0), filePath)
            #return [p.]
            self.counter+=1
        elif self.counter >= self.len_1 and self.counter < self.len_2:
            current_permutation = self.list_two[self.counter - self.len_1]
            scad_render_to_file(cylinder(h=current_permutation[0], r1=current_permutation[1], r2=current_permutation[1]), filePath)
            #return [p.GEOM_CYLINDER, current_permutation[0], current_permutation[1]]
            self.counter += 1
        elif self.counter >= self.len_2 and self.counter < self.len_3:
            current_permutation = self.list_three[self.counter - self.len_2]
            scad_render_to_file(cube(size=(current_permutation[0], current_permutation[1], current_permutation[2])), filePath)
            #return [p.GEOM_BOX, [current_permutation[0], current_permutation[1], current_permutation[2]]]
            self.counter += 1
        elif self.counter >= self.len_3 and self.counter < self.len_4:
            current_permutation = self.list_three[self.counter - self.len_3]
            scad_render_to_file(scale([current_permutation[0], current_permutation[1], current_permutation[2]])(sphere(r=current_permutation[3])), filePath)
            #return [p.GEOM_SPHERE, ]
            self.counter += 1
        else:
            print("Error in resize: index past number of permutatations")