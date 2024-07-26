counter = 1

for i in range(1000):
    counter = counter * 2

counter_s = str(counter)

result = 0

for character in counter_s:
    result += int(character)

print(result)

# Solution: 1366