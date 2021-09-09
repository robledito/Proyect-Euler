prim = []
i = 1
while len(prim) < 1000:
    i += 1
    if all(i % prime != 0 for prime in prim):
        prim.append(i)
uwu = {2*n +1 for n in range(1, 100000)}
jpo = set()
for i in range(0,1000):
    for a in prim:
        jpo.add(a + 2*(i**2))
temp2 = set(uwu)
a = uwu.difference(jpo)
print(min(a))