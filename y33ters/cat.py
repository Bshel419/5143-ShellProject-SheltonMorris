import os

def cat(command, flags, params):
    with open(params[0]) as treasure:
        for line in treasure:
            print(line)
    return