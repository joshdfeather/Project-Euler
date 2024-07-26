from math import ceil
from math import sqrt

numbers = {}

for i in range(10000):

    counter = - i

    for j in range(1, ceil(sqrt(i)) + 1):

        if j == sqrt(i):
            counter += j

        elif i % j == 0:
            counter += j
            counter += int(i / j)
        
    
    numbers[i] = counter

total = 0

for i in range(10000):
    for j in range(10000):
        if numbers[i] == j and numbers[j] == i and i != j:
            total += (i + j)   

print(int(total / 2))


# Solution: 31626