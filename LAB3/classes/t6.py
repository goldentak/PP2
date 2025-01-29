#6  |   Write a program which can filter prime numbers
numlist = range(1, 51)
filt = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))


primeNumbers = [x for x in numlist if filt(x)]
print(primeNumbers)