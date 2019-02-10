import os

path = '.'

def mkdir(name):
    try:
        os.mkdir(path + name)
    except OSError:
        print("Cannot create " + name + " directory")
    return