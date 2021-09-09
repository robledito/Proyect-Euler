import math
import time
start_time = time.time()
def sumdiv(n):
    sumdiv = 1
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            sumdiv = sumdiv + i
    return sumdiv
sumatot = 0
lista = set([a for a in range(1,10000)])
quitados = set()
for a in range(1,10000):
    for b in lista.difference(quitados):
        if (sumdiv(a) == b and sumdiv(b) == a) and a != b:
            sumatot = sumatot + a + b
            quitados.add(b)
print(sumatot)
print("--- %s seconds ---" % (time.time() - start_time))