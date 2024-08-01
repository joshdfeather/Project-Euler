
total = 0

for i in range(2, 300000):

    if i == sum((int(n) ** 5) for n in str(i)):
        total += i

print(total)

# Solution: 443839