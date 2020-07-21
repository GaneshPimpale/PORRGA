import os
from pyodm import Node

print("Creating Node connection")
nd = Node("localhost", 3000)

print("Creating ODM task")
path = os.path.realpath("images")

image_list = [path + "/1-1.jpg",
              path + "/1-2.jpg",
              path + "/1-3.jpg"]

task = nd.create_task(image_list, {'orthophoto-resolution': 2, 'dsm': True})
print("Running task")
task.wait_for_completion()
os.listdir(task.download_assets("results"))



