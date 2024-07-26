
palendromes = []
counter  = 0

def palendrome(a):

    b = str(a)

    c = []

    d = []

    for i in range(len(b)):
        c.append(b[i])

    for j in range(len(b)):
        d.insert(0, b[j])

    if c == d:
        return a



for x in range(1, 1000000):

        y = str(x)

        if palendrome(y) != None:
            palendromes.append(x)


for pal in palendromes:

    j = int(str(bin(pal)[2:]))

    if palendrome(j) != None:
        counter += pal


print(counter)

# Solution: 872187