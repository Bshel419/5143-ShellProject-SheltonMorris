from shutil import copyfile

path = '.'

def cd(old, new):
    try:
        copyfile(old, new)

    except IOError:
        print("Destination location (" + new + ") is not writable")