
from math import ceil
from math import sqrt

counter = 0


for i in range(10000):
    
    for j in range(2, ceil(sqrt(i)) + 1):

        if (i % j == 0):
            if '1' in (str(i) + str(j) + str(i / j)) and '2' in (str(i) + str(j) + str(i / j)) and '3' in (str(i) + str(j) + str(i / j)) and '4' in (str(i) + str(j) + str(i / j)) and  '5' in (str(i) + str(j) + str(i / j)) and '6' in (str(i) + str(j) + str(i / j)) and '7' in (str(i) + str(j) + str(i / j)) and '8' in (str(i) + str(j) + str(i / j)) and '9' in (str(i) + str(j) + str(i / j)):
                counter += i
                break

print(counter)

# Solution: 45228