from math import sqrt


tri = 0

for i in range(1, 15000):
    tri += i

    divs = [1, tri]

    for j in range (2, int(sqrt(tri)) + 1):
        if (tri % j == 0) and j not in divs and (tri / j not in divs):
            divs.extend([j, tri / j])

    if len(divs) > 500:
        print(tri)


# Solution: 76576500