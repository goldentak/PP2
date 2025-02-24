file_name = 'LAB6/dir-and-files/example.txt'

file = open(file_name)

a = 0
for line in file:
    a += 1

print(a)