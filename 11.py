grid = []

with open("text.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        grid.append(line.strip().split(' '))

counter_d1 = 0
counter_d2 = 0
counter_h = 0
counter_v = 0

# Check leading diagonal

for i in range(17):
    for j in range(17):
        product_d2 = int(grid[i][j]) * int(grid[i + 1][j + 1]) * int(grid[i + 2][j + 2]) * int(grid[i + 3][j + 3])
        if product_d2 > counter_d2:
            counter_d2 = product_d2

# Check non-leading diagonal

for i in range(20):
    for j in range(3, 17):
        product_d1 = int(grid[i - 3][j + 3]) * int(grid[i][j]) * int(grid[i - 1][j + 1]) * int(grid[i - 2][j + 2])
        if product_d1 > counter_d1:
            counter_d1 = product_d1

# Check vertical

for i in range(17):
    for j in range(20):
        product_v = int(grid[i][j]) * int(grid[i + 1][j]) * int(grid[i + 2][j]) * int(grid[i + 3][j])
        if product_v > counter_v:
            counter_v = product_v

# Check horizontal

for i in range(20):
    for j in range(17):
        product_h = int(grid[i][j + 1]) * int(grid[i][j + 2]) * int(grid[i][j + 3]) * int(grid[i][j])
        if product_h > counter_h:
            counter_h = product_h

print(counter_d2)
print(counter_h)
print(counter_v)
print(counter_d1)

# Solution : 70600674
