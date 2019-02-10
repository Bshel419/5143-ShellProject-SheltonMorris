import os

def cat(name, files):
    with open(name) as treasure:
        for line in treasure:
            print(line)
    return