import os

path = '.'

def ls(command, flags, params, output):
    
    files = os.listdir(path)
    if not output:
        for file in files:
            print(file)
    else:
        with open(output[0], 'w') as outfile:
            for file in files:
                outfile.write(file)
    return 



