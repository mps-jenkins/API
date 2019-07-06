import os

def listdir(dirname):
    basedir = dirname
    for file in os.listdir(dirname):
        path = os.path.join(basedir, file)
        if os.path.isdir(path):
            print("Directory",path)
        elif os.path.isfile(path):
            print("File", path)



listdir("/home/s.verma1/Documents")