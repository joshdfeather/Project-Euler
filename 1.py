
counter = 0

integer = 1

while integer < 1000:

    if integer % 3 == 0:

        counter = counter + integer

    elif integer % 5 == 0:

        counter = counter + integer
        
    integer += 1

print(counter)

# Solution: 233168