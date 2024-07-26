
def cycle_length(denominator):
    numerator = 1
    remainders = []

    while len(remainders) == len(set(remainders)):

        remainder = numerator % denominator
        remainders.append(remainder)
        numerator = remainder * 10

    return len(set(remainders))

counter = 0
max_num = 0

for i in range(2, 1000):
    if cycle_length(i) > counter:
        counter = cycle_length(i)
        max_num = i

print(max_num)

# Solution: 983