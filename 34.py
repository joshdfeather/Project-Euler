
def factorial(x):

    counter = 1

    while x != 0:

        counter = counter * x
        x -= 1

    return counter

sums = 0

for i in range(3, 50000):

    count = 0

    j = str(i)

    for k in range(len(j)):
        count += factorial(int(j[k]))

    if count == i:
        sums += i

print(sums)

# Solution: 40730