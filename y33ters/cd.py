import os

path = '.'

def cd(directory=None, homeFlag=None, backFlag=None):
    if directory != None:
        try:
            os.chdir(path + directory)
        except OSError:
            print("ERROR: " + directory + " directory not found" )
    elif homeFlag != None:
        os.chdir('~')
    elif backFlag != None:
        os.chdir('..')
    else:
        os.chdir('~')