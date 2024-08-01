
from itertools import count


perimeters = []

mostps = 0

most = 0

for a in range(1, 500):
    for b in range(1,500):
        c = (a**2 + b**2)** 0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(int((a + b + c)))

for perimeter in perimeters:

    if perimeters.count(perimeter) > mostps:
        mostps = perimeters.count(perimeter)
        most = perimeter
    
print(most)

# Solution: 840