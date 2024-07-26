


def prime(x):

    for i in range(2, x + 1):

        if (x % i) == 0 and i != x:
            break

        elif i == x:
            return x


counter = 0

for i in range(2, 2000000):

    if prime(i) is None:
        continue

    else:
        counter = counter + prime(i)

print(counter)

# Solution: 142913828922
