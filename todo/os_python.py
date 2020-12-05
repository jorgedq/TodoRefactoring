import os

# option one
home_path = dict(os.environ)["HOME"]

new_path = "{}/Escritorio/new_carpet".format(home_path)

file_ = "file.txt"

name_file = "{}/{}".format(new_path, file_)

with open(name_file, "w+") as test:
    test.write("this is the new task for the finally test")
    test.write("delete this task")

