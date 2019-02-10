import os

path = '.'

def ls(aFlag=None, lFlag = None, hFlag = None):
    files = os.listdir(path)

    for file in files:
        print(file)
    return 



