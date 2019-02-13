import os


def rmdir (command, flags, params):
    try:
        os.rmdir(params[0])
    except OSError:
        print("The directory" + path + "is not empty.")
    return