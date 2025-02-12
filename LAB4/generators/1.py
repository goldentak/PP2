#Create a generator that generates the squares of numbers up to some number N.
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

N = int(input("write some natural number:: "))
for square in square_generator(N):
    print(square)