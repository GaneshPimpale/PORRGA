import pybullet as p
import pandas as pd


class getTorque:
    def __init__(self, id):
        numJoints = p.getNumJoints(id)
        dict = {}
        for i in range(numJoints):
            temp = p.getJointState(id, i)
            dict['Joint #' + str(i+1)] = temp[3]
            indices = ['Torque']
        return pd.DataFrame(dict, index=indices).to_csv('torques.csv')