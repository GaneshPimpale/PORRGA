# import SolidPython package
from solid.import *
from solid.utils import *
from random import randint

class Resize:
    # import OpenScad code (file name corresponds to shape)
    scadFile = import_scad('/path/to/example.scad')
    # classify shape + parameters
    if scadFile == 'cone.scad':
        def __init__(self, shape, r1, r2, h):
            self.shape = shape
            self.r1 = r1
            self.r2 = r2
            self.h = h
        shape = 'cone'
    elif scadFile == 'cylinder.scad':
        def __init__(self, shape, r1, r2, h):
            self.shape = shape
            self.r1 = r1
            self.r2 = r2
            self.h = h
        shape = 'cylinder'
    elif scadFile == 'rectangularPrism.scad':
        def __init__(self, shape, h, w, l):
            self.shape = shape
            self.h = h
            self.w = w
            self.l = l
        shape = 'r_prism'
    else:
        def __init__(self, shape, r, h):
            self.shape = shape
            self.r = r
            self.h = h
        shape = 'ellipse'

    # resize parameters / shape using for loop, random
    i = 1
    if shape == 'cone':
        for i in range(10):
            r1 = randint(1, 10)
            r2 = 0
            h = randint(1, 10)
            scad = scadFile.cylinder(r1, r2, h)
    elif shape == 'cylinder':
        for i in range(10):
            r1 = randint(1, 10)
            r2 = randint(1, 10)
            h = randint(1, 10)
            scad = scadFile.cylinder(r1, r2, h)
    elif shape == 'r_prism'
        for i in range(10)
            h = randint(1, 10)
            w = randint(1, 10)
            l = randint(1, 10)
            scad = scadFile.box(h, w, l)
    else:
        for i in range(10)
            r = randint(1, 10)
            h = randint(1, 10)
            scad = scadFile.ellipsis(r, h)

# render to file (STL/scad)
    scad_render_to_file(scad, 'example.scad')