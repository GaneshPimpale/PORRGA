import pybullet as p
import pandas as pd


class getJointValues:
    def __init__(self, id):
        numJoints = p.getNumJoints(id)
        dict = {}
        for i in range(numJoints):
            temp = p.getJointState(id, i)
            dict['Joint #' + str(i+1)] = [temp[3], temp[0]]
            indices = ['Torque', 'Position']
        return pd.DataFrame(dict, index=indices).to_csv('jointValues.csv')