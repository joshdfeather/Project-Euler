from random import randint

triangle = []

with open('triangle.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        triangle.append(line.strip().split(' '))

print(triangle)

products = []

for i in range(20000):

    product = 0
    k = 0

    for j in range(15):

            product += int(triangle[j][k])
            k += randint(0, 1)

    products.append(product) 

print(max(products))  

# Solution: 1074

