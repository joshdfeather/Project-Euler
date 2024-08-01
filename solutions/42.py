from itertools import permutations
from time import time

perms = list(permutations('0123456789'))

def sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate prime numbers from m up to n (non-inclusive)
    """
    sieve = [True] * n

    for p in range(2, n):

        if sieve[p] is True:

            for i in range(p*p, n, p):
                
                sieve[i] = False

    primes = []

    for i in range(m, n):

        if sieve[i] is True:
            primes.append(i)

    if 1 in primes:
        primes.remove(1)
    
    return primes

primes = sieve(2,20)

count = 0


for perm in perms:

    counter  = 0

    for i in range(7):
        if int(str(perm[i + 1]) + str(perm[i + 2]) + str(perm[i + 3])) % primes[i] == 0:
            counter += 1
    
    if counter == 7:
        count += int(''.join(perm))

print(count)

# Solution: 16695334890 taking 24.8s