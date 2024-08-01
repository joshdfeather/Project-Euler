from math import ceil
from math import sqrt
from time import time

start = time()

def prime(x):

    for num in range(2, ceil(sqrt(x)) + 1):

        if (x % num) == 0 and num != ceil(sqrt(x)):
            break

        elif num == ceil(sqrt(x)) and num != sqrt(x):
            return x

primes = []

for i in range(2, ceil(sqrt(600851475143)) + 1):

    if prime(i) != None:
        primes.append(i)

for prime in primes:
    if 600851475143 % prime == 0:
        maxprime = prime

print(maxprime)
print(time() - start)

# Solution: 6857
