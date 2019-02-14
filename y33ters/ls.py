import os

path = '.'

def ls(command, flags, params, output):
    files = os.listdir(path)
    
    for file in files:
        print(file)
    return 



