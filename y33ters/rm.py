import os

path = '.'

def rm (command, flags, params, output):
    if os.path.exists(params[0]):
        try:
            os.remove(params[0])
        except OSError:
            print("Cannot delete directories")
    else:
        print("This file does not exist")
    return