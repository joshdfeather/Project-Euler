stri = ''

product = 1

for i in range(1, 25000):
    stri = stri + str(i)

product = product * int(stri[0])  * int(stri[9]) * int(stri[99])  * int(stri[999]) * int(stri[9999])  * int(stri[99999]) 

print(product)

# Solution: 210