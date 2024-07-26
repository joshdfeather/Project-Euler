from itertools import permutations

perms = sorted([int(''.join(c for c in n)) for n in list(permutations("0123456789"))])

print(perms[999999])

# Solution: 2783915460