import y33ters as yt
import os


if __name__ == "__main__":
    
    commandDic = { 
        'cat': yt.cat,
        'cd': yt.cd,
        'cp': yt.cp,
        'grep': yt.grep,
        'head': yt.head,
        'less': yt.less,
        'ls': yt.ls,
        'mkdir': yt.mkdir,
        'mv': yt.mv,
        'pwd': yt.pwd,
        'rm': yt.rm,
        'rmdir': yt.rmdir,
        'sort': yt.sort,
        'tail': yt.tail,
        'wc': yt.wc,
        'who': yt.who
    }
    

    argsDic = {"Command": [], "Params": [], "Flags": [], "Output":[]}
    history = []

    loop = True

    while(loop):
        print(os.getcwd())
        cmd = input(">> ")
        history.append(cmd)

        cmd = cmd.split()
        
        print(cmd)

        if cmd[0] == "cd":
            commandDic["cd"]()

        if cmd[0] == "REEE":
            loop = False

