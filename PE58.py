from sympy import prime # Tarda

prim = []
i = 0

while i < 100000:
    i += 1
    prim.append(prime(i))

valor = 1        
i = 5

while (valor >= 0.1):
        elementos = [x for x in range(1,i+1) if x % 2 == 1]
        primos_diag = []
        for j in range(len(elementos)):
            if (j != range(len(elementos))[-1]) and (j != 0):
                ini = (elementos[j])**2
                fin = (elementos[j+1])**2
                rango = range(ini, fin+1)
                salto = (fin - ini)/4
                primos_diag.append(ini)
                primos_diag.append(int(ini + salto))
                primos_diag.append(int(ini + 2*salto))
                primos_diag.append(int(ini + 3*salto))
            elif i == 0:
                primos_diag.extend([3,5,7,9])
            else:
                fin = (elementos[-1])**2
                primos_diag.append(fin)
        
        primos_diag = [x for x in primos_diag if x in prim]

        valor = len(primos_diag)/(2*i-1)
        i +=2
        
print(i)