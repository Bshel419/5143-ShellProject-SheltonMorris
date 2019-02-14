import os
import re

def grep(command, flags, params, output):
    with open(params[0]) as treasure:
        for line in treasure:
            line = re.findall(params[1], line)
            print(line)
    return