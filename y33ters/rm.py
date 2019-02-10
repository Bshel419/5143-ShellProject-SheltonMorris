import os

path = '.'

def rm (name):
    if os.path.exists(name):
        try:
            os.remove(name)
        except OSError:
            print("Cannot delete directories")
    else:
        print("This file does not exist")
    return