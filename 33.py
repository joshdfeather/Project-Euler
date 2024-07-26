numerator = 1
denominator = 1

for i in range(10, 100):
    for j in range(10, 100):

        if i < j and i % 10 != 0 and j % 10 != 0:

            a = str(i)
            b = str(j)

            if a[0] == b[0]:

                c = int(a[1])
                d = int(b[1])

                if c != 0 and d != 0 and c / d == i / j:

                    numerator = numerator * c
                    denominator = denominator * d

            elif a[1] == b[0]:

                c = int(a[0])
                d = int(b[1])

                if c != 0 and d != 0 and c / d == i / j:

                    numerator = numerator * c
                    denominator = denominator * d

            elif a[1] == b[1]:

                c = int(a[0])
                d = int(b[0]) 

                if c != 0 and d != 0 and c / d == i / j:

                    numerator = numerator * c
                    denominator = denominator * d

            elif a[0] == b[1]: 

                c = int(a[1])
                d = int(b[0])

                if c != 0 and d != 0 and c / d == i / j:

                    numerator = numerator * c
                    denominator = denominator * d

print(numerator)
print(denominator)

# Solution: 100
            
            