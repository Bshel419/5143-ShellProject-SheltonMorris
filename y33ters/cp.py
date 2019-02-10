from shutil import copyfile

def cp(old, new):
    try:
        copyfile(old, new)
    except IOError:
        print("Destination location (" + new + ") is not writable")
    return