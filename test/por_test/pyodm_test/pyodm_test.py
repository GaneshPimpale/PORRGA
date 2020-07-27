import os
from pyodm import Node

print("Creating Node connection")
nd = Node("localhost", 3000)

print("Creating ODM task...")
path = os.path.realpath("images")
image_list = [path + "/1-1.jpg",
              path + "/1-2.jpg",
              path + "/1-3.jpg",
              path + "/1-4.jpg",
              path + "/1-5.jpg",
              path + "/1-6.jpg",
              path + "/1-7.jpg",
              path + "/1-8.jpg",
              path + "/1-9.jpg",
              path + "/1-10.jpg",
              path + "/1-11.jpg"]

image_list_1 = [path + "/1-1.jpg",
                path + "/1-2.jpg",
                path + "/1-3.jpg"]

task = nd.create_task(image_list_1)

print("Running task...")
task.wait_for_completion()

print("Completed")
os.listdir(task.download_assets("results"))



