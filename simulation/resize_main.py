import resize


files = ['cone.scad', 'cylinder.scad', 'ellipse.scad', 'rectangularPrism.scad']
for file in files:
    test = resize.Resize(file)
    test.iterate()
    test.assign
    print(test.scad_file)