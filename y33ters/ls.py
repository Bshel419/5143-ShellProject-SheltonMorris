import os

path = '.'

def ls(command, flags, params):
    files = os.listdir(path)
    
    for file in files:
        print(file)
    return 



