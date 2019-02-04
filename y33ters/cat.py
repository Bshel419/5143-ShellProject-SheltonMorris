import os
import webbrowser

path = '.'

def cat(name, files):
    i = 0
    while i < files:
        webbrowser.open(name)
        i += 1