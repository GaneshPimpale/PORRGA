import time
import pybullet as p
import pybullet_data
import torque

class simulation:
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    handID = p.loadURDF("C:/Users/ehuan/Desktop/SHTEM/PORRGA/simulation/Hand-Assem-By-Part-URDF.SLDASM/urdf/Hand-Assem-By-Part-URDF.SLDASM.urdf", useFixedBase=True, flags= p.URDF_USE_SELF_COLLISION)
    for i in range(p.getNumJoints(handID)):
        p.enableJointForceTorqueSensor(handID, i)
    torque.getTorque(handID)
    for i in range (10000):
        p.stepSimulation()
        time.sleep(1./240.)
    p.disconnect()