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

primes = sieve(2, 10000000)

maximum = []

for prime in primes:
    if (sorted(list(str(prime)))) == ['1', '2', '3', '4', '5', '6', '7']:
        maximum.append(prime)

print(max(maximum))

# Solution: 7652413
