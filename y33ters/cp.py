from shutil import copyfile

def cp(command, flags, params):
    try:
        copyfile(params[0], params[1])
    except IOError:
        print("Destination location (" + new + ") is not writable")
    return