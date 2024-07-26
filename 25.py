
num1 = 1
num2 = 1
num3 = 0

numbers = [1, 1, ]

while len(str(num3)) < 1000:

    num3 = num1 + num2

    numbers.append(num3)

    num1 = num2
    num2 = num3

print(len(numbers))

# Solution: 4782