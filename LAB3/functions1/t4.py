# 4  |  Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
import math
def filter_prime(a = []):
    primes = []
    for i in a:
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0: 
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

a = list(range(1, 51))

print(filter_prime(a))