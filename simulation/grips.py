import numpy as np

# for each grip type, return the final hand position given size/position of object.
# hand position defined as 21-length array of final joint positions maybe
class grips:

    # 2 finger grip
    def smallCone(position, radius, height):
        return np.zeros(21)

    # full palm grasp
    def cone(position, radius, height):
        return np.zeros(21)

    # 2 finger grip at each base
    def smallCyliner(position, radius, height):
        return np.zeros(21)

    # full palm grasp of side
    def cylinder(position, radius, height):
        return np.zeros(21)

    # 2 finger grip of longer sides
    def smallEllipsoid(position, radius, scale_factors):
        return np.zeros(21)

    # full palm grasp
    def ellipsoid(position, radius, scale_factors):
        return np.zeros(21)

    # 2 finger grip
    def smallRectangularPrism(position, width, length, height):
        return np.zeros(21)

    # grasp
    def rectangularPrism(position, width, length, height):
        return np.zeros(21)