from itertools import permutations

solutions = []


def pathcounter(grid):
    path = []

    counter = 0

    for i in range(grid):
        path.append(0)
        path.append(1)

    for j in permutations(path, grid * 2):
        if j not in solutions:
            print(j)
            solutions.append(j)
            counter += 1

    return counter


print(pathcounter(20))

# Solution: 137846528820
