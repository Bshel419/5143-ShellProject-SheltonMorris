import os

path = '.'

def pwd(aFlag=None, lFlag = None, hFlag = None):
    name = os.path.dirname(path)
    print(name)