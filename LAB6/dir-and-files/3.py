import os

path = '/Users/VSCODE'
if os.access(path, os.F_OK):
    filename = os.path.basename(path)
    print(filename)
else:
    print('Exist:', os.access(path, os.F_OK))