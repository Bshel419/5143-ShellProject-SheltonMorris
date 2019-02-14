import os

def head(command, flags, params):
    with open(params[0]) as treasure:
        treasure = treasure.readlines()
        for x in range(int(params[1])):
            print(treasure[x])
    return
                