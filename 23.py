
from math import ceil
from math import sqrt

numbers = {}

def divisors(n: int) -> list:
    """
    Returns all the divisors of a given integer (non-inclusive)
    """
    divs = [1]
    for i in range(2, ceil(sqrt(n)) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            divs.extend([i, n / i])
    return set(divs)


for i in range(2, 28124):
    total = 0
    divs = divisors(i)
    for j in range(len(divs)):
        total += int(list(divs)[j])

    numbers[i] = total


abundants = []


zeros = []

for i in range(28124):
    zeros.append(0)

for i in range(2, 28124):
    if numbers[i] > i:
        abundants.append(i)

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= 28123:
            zeros[abundants[i] + abundants[j]] = 1

counter = 0

for i in range(len(zeros)):
    if zeros[i] == 0:
        counter += i

print(counter)


