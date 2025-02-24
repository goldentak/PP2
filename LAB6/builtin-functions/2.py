s = "Hello World"
a = 0
b = 0
for i in s:
    if i.isupper():
        a += 1
    elif i.islower and i != " ":
        b += 1

print(a, b)