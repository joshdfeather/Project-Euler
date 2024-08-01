
primes = []


def prime(x):
    for i in range(2, x + 1):

        if (x % i) == 0 and i != x:
            break

        elif i == x:
            return x


for i in range(150000):

    if prime(i) is None:
        continue
    else:
        primes.append(prime(i))

print(primes[10000])

# Solution: 104743
