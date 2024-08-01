
palendromes = []

for i in range(100, 1000):
    for j in range(100, 1000):

        x = i * j

        y = str(x)

        length = len(y)

        if ((y[0] == y[length - 1]) and (y[1] == y[length - 2]) and y[2]) == y[length - 3]:
            palendromes.append(int(y))

print(max(palendromes))

# Solution: 906609