import os

def cat(command, flags, params, output):
        
        for f in params:
                with open(f) as treasure:
                        if not output:
                                for line in treasure:
                                        print(line)
                        else:
                                with open(output[0], "w") as outfile:
                                        for line in treasure:
                                                outfile.write(line)

        return