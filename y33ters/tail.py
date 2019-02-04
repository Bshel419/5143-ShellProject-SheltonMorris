import os

def tail(name, num):
    while num > 0:
        with open(name) as treasure:
            for line in treasure:
                print(line)
                num -=1