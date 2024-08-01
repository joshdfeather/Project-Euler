
names = []

with open("names.txt", "r") as file:
    for name in file.read().split(','):
        names.append(name[1:-1])


sorted_names = sorted(names)

count = 0

for i in range(len(sorted_names)):

    counter = 0

    for j in sorted_names[i]:

        counter += ord(j) - 64

    count += (i + 1) * counter

print(count)

# Solution: 871198282