
spiral = []

for i in range(1, 1002002):
    spiral.append(i)

evens = []

for j in range(1, 1001):
    if j % 2 == 0:
        evens.append(j) 

k = 0

counter = 1

for l in range(500):
    for i in range(4):
        k += evens[l]
        counter += spiral[k]
        

print(counter)

# Solution: 669171001