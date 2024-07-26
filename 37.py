from math import ceil
from math import sqrt


def prime(x):

    for num in range(2, ceil(sqrt(x)) + 1):

        if (x % num) == 0 and num != ceil(sqrt(x)):
            break

        elif num == ceil(sqrt(x)) and num != sqrt(x):
            return x

primes = []

count = 0

for i in range(11, 1000000):

    if prime(i) != None:
        primes.append(i)

for pri in primes:

    counter = 0
    
    a = str(pri)
    c = str(pri)

    while len(a) != 1:

        a = a[:-1]

        c = c[1:]


        if prime(int(a)) != None and prime(int(c)) != None:
            counter += 1


    if counter + 1 == len(str(pri)):
        count += pri

print(count)

# Solution: 748317
