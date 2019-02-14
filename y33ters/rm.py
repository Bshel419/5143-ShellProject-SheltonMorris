import os

path = '.'

def rm (command, flags, params, output):
    if os.path.exists(name):
        try:
            os.remove(name)
        except OSError:
            print("Cannot delete directories")
    else:
        print("This file does not exist")
    return