
class number:

    def __init__(self, current, previous):
        self.current = current
        self.previous = previous


num2 = number(2, 1)

num3 = number(0, 0)

counter = 2

while num3.current < 4000000:

    num3.current = num2.current + num2.previous
    num3.previous = num2.current

    num2.current = num3.current
    num2.previous = num3.previous

    if num3.current % 2 == 0:
        counter = counter + num3.current

print(counter)

# Solution: 4613732