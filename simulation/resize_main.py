import resize

test = resize.Resize('cone.scad')
test.iterate()
test.assign
print(test.scad_file)