#Implement a generator that returns all numbers from (n) down to 0.
def decrease(n):
    while(n != 0):
        yield n
        n -= 1

n = int(input("Enter number n:: "))

for num in decrease(n):
    print(num)