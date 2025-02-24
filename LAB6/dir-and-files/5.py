lst = [1, 2, 3, 4]

file_name = 'LAB6/dir-and-files/file1.txt'
with open(file_name, 'w') as f:
    for i in lst:
        f.write(str(i)+ " ")