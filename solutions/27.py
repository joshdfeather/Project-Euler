from math import ceil
from math import sqrt



def prime(x):

    for num in range(2, ceil(sqrt(x)) + 1):

        if (x % num) == 0 and num != ceil(sqrt(x)):
            break

        elif num == ceil(sqrt(x)) and num != sqrt(x):
            return x


primes_less_than_1000 = []


for i in range(1000):
    if prime(i) != None:
        primes_less_than_1000.append(i)


largest = 0

for a in range(1, 1000):
    for b in primes_less_than_1000:

        n = 0

        # Positive a and b

        while True:

            quadratic = abs((n * (n + a)) + b)

            if prime(quadratic) == None:

                if n - 1 > largest:

                    largest = n - 1
                    ab = a * b

                break

            n += 1

        # Positive b and negative a

        while True:

            quadratic = abs((n * (n - a)) + b)


            if prime(quadratic) == None:

                if n - 1 > largest:
                    largest = n - 1
                    ab = - (a * b)

                break

            n += 1
            
print(ab)

# Solution : -59231
