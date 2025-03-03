s = "Hello World"
a = 0
b = 0
for i in s:
    if 65 <= ord(i) <= 90:
        a += 1
    elif 97 <= ord(i) <= 122:
        b += 1

print(a, b)
