import time
from sympy import prime

start_time = time.time()
prim = set()
i = 0

while i < 100000:
    i += 1
    prim.add(prime(i))
    
print(sum(prim))
print("--- %s seconds ---" % (time.time() - start_time))