from shutil import move

path = '.'

def mv(old, new):
    try:
        move(old, new)

    except IOError:
        print("Destination location (" + new + ") is not writable")