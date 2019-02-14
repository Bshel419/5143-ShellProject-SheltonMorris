import os

def cat(command, flags, params):
        for f in params:
                with open(f) as treasure:
                        for line in treasure:
                                print(line)
                print()
        return