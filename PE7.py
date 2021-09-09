prim = []

i = 1

while len(prim) < 10001:
    i += 1
    if all(i % prime != 0 for prime in prim):
        prim.append(i)
        
print(prim[-1])