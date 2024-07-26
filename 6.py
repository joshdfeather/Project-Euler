
counter_squares = 0
counter_sum = 0

for i in range(101):
    counter_squares = counter_squares + (i * i)

for i in range(101):
    counter_sum = counter_sum + i

result = (counter_sum * counter_sum) - counter_squares

print(result)

# Solution: 25164150

