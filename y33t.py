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
        cmd = input(">> ")
        history.append(cmd)

        cmd = cmd.split()

        if cmd[0] == "REEE":
            loop = False
        elif cmd[0] == "history":
            for line in history:
                print(line)
        else:
            for arg in cmd:
                if arg in commandDic:
                    argsDic["Command"].append(arg)
                elif arg[0] == '-':
                    argsDic["Flags"].append(arg)
                else:
                    argsDic["Params"].append(arg)

            commandDic[cmd[0]](argsDic["Command"], argsDic["Flags"], argsDic["Params"])

        argsDic.clear()
        cmd = []

