"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time
start_time = time.time()


suma = 0

elementos = [x for x in range(1,1001+1) if x % 2 == 1]

for i in range(len(elementos)):
    if (i != range(len(elementos))[-1]) and (i != 0):
        ini = (elementos[i])**2
        fin = (elementos[i+1])**2
        rango = range(ini, fin+1)
        salto = (fin - ini)/4
        suma += (ini)
        suma += (3*ini + 6*salto)
    elif i == 0:
        suma += 16
    else:
        fin = (elementos[-1])**2
        suma += fin
        break

print(suma)
print("--- %s seconds ---" % (time.time() - start_time))

# Nota: al parecer se puede hacer en una sola línea usando el hecho de que los lados cumplen cierta relación