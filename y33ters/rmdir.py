import os

path = '.'

def rmdir (path):
    try:
        os.rmdir(path)
    except OSError:
        print("The directory" + path + "is not empty.")