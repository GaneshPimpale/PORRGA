import time
import pybullet as p
import pybullet_data
import jointValues
import resize

class simulation:
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    #shapeID = p.createCollisionShape(shapeType=p.GEOM_SPHERE, radius=0.05)
    handID = p.loadURDF("Hand-Assem-By-Part-URDF.SLDASM/urdf/Hand-Assem-By-Part-URDF.SLDASM.urdf", basePosition=[0,0,0], useFixedBase=True, flags= p.URDF_USE_SELF_COLLISION)
    #p.createMultiBody(baseMass=1, baseCollisionShapeIndex=shapeID, basePosition=[0.5, 0.5, 0.5])
    shapeID = p.loadURDF("Hand-Assem-By-Part-URDF.SLDASM/urdf/Example Sphere.urdf")
    for i in range(p.getNumJoints(handID)):
        p.enableJointForceTorqueSensor(handID, i)
    resizeObj = resize.Resize(range(3, 20, 2))

    while True:
        p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING)

        resizeObj.iterate()
        shapeID = p.loadURDF("Hand-Assem-By-Part-URDF.SLDASM/urdf/Example Sphere.urdf")
        jointValues.getJointValues(handID)
        p.stepSimulation()
        time.sleep(1./240.)

    p.disconnect()