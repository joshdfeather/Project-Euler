list = []

for i in range(500):
    for j in range(500):
        for k in range(500):

            if ((i * i) + (j * j) == (k * k)) and ((i + j + k) == 1000):
                I = str(i)
                J = str(j)
                K = str(k)
                list.append(I)
                list.append(J)
                list.append(K)

print(int(list[0]) * int(list[1]) * int(list[2]))

# Solution: 31875000 (200, 375 and 425)
