numbers = []

with open("number.txt") as file:
    for line in file.readlines():
        numbers.append(int(line.strip()))

print(str(sum(numbers))[:10])

# Solution: 5537376230