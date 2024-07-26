from math import ceil
from math import sqrt


def prime(x):

    for num in range(2, ceil(sqrt(x)) + 1):

        if (x % num) == 0 and num != ceil(sqrt(x)):
            break

        elif num == ceil(sqrt(x)) and num != sqrt(x):
            return x

def rotation(n):

    rotations = set()

    for i in range(len(str(n))):

        m = int(str(n)[i:] + str(n)[:i])
        rotations.add(m)

    return list(rotations)

primes = []

for i in range(1000000):

    if prime(i) != None:
        primes.append(i)

count = 0

for a in range(len(primes)):


    if '0' not in str(primes[a]):

        c = rotation(primes[a])

        counter = 0

        for b in c:

            if prime(b) != None:
                counter += 1

        if counter == len(c):
            count += 1

print(count)

# Solution: 55
