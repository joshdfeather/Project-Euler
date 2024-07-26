
lst = []

for i in range(1, 10000):

    product = ''

    for j in range(1, 10):
        
        product += str(i * j)

        sort = sorted(product)

        stri = ''.join(sort)
        
        if stri == '123456789':
            lst.append(int(product))


print(max(lst))

# Solution: 932718654

