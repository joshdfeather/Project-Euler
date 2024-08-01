product = 1

for i in range(100):
    product = product * (i + 1)

string = str(product)
counter = 0

for j in range(len(string)):
    counter += int(string[j])

print(counter)

# Solution: 648