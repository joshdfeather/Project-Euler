from math import sqrt
from math import ceil


def prime(x):

    for num in range(2, ceil(sqrt(x)) + 1):

        if (x % num) == 0 and num != x:
            break

        elif num == ceil(sqrt(x)):
            return x

counter = 5

for i in range(4, 2000000):

    if i % 2 == 0:
        continue

    elif prime(i) is None:
        continue

    else:
        counter = counter + i

print(counter)

# Solution: 142913828922
