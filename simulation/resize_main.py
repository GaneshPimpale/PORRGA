import resize


files = ['cone.scad', 'cylinder.scad', 'ellipse.scad', 'rectangularPrism.scad']

test = resize.Resize(files[1], range(3, 20, 2))
test.iterate()
test.iterate()
test.iterate()
test.iterate()
print(test.scad_file)