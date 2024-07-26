def generate(x):

    sequence = [x]

    sequence.append(str(x))

    while x != 1:

        if x % 2 == 0:
            sequence.append(str(int((x / 2))))
            x = (x / 2)

        elif x % 2 == 1:
            sequence.append(str(int((3 * x) + 1)))
            x = (3 * x) + 1

    return sequence


counter = 0

for i in range(1, 1000000):
    if len(generate(i)) > counter:
        counter = len(generate(i))
        print(i)

# Solution: 837799