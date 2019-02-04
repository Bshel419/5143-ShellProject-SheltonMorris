import os
import re

def grep(key, name):
    with open(name) as treasure:
        for line in treasure:
            line = re.findall(key, line)
            print(line)