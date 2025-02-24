#copy all text from the example to file2

filefrom = 'LAB6/dir-and-files/example.txt'
fileto = 'LAB6/dir-and-files/file2.txt'

with open(filefrom, 'r') as file:
    content = file.read()

with open(fileto, 'a') as file:
    file.write(content)