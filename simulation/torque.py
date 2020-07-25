import pybullet as p
import time
import pybullet_data
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

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
handID = p.loadURDF("C:/Users/ehuan/Desktop/SHTEM/PORRGA/simulation/Hand-Assem-By-Part-URDF.SLDASM/urdf/Hand-Assem-By-Part-URDF.SLDASM.urdf", useFixedBase=True, flags= p.URDF_USE_SELF_COLLISION)
for i in range(p.getNumJoints(handID)):
    p.enableJointForceTorqueSensor(handID, i)
getTorque(handID)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
p.disconnect()

