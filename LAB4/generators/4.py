#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter the start number:: "))
b = int(input("Enter the end number:: "))

for square in squares(a, b):
    print(square)
