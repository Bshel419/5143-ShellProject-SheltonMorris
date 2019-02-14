from shutil import move

path = '.'

def mv(command, flags, params, output):
    try:
        move(old, new)

    except IOError:
        print("Destination location (" + new + ") is not writable")
    return