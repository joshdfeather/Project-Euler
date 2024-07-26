
counter = 1

for a in range(3): # 100p coins
    for b in range( int(1 + ((200 - (100 * a)) / 50)) ): # 50p coins
        for c in range( int(1 + ((200 - (100 * a) - (50 * b)) / 20)) ): # 20p coins
            for d in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c)) / 10)) ): # 10p coins
                for e in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c) - (10 * d)) / 5)) ): # 5p coins
                    for f in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c) - (10 * d) - (5 * e)) / 2)) ): # 2p coins
                        counter += 1 # the rest are made by 1p 
                    
print(counter)

# Solution: 73682