import fractions
import time
start_time = time.time()
def num(n):
    if n in range(11,101):
        i = 2
        while  fractions.Fraction((10**i), n) - int(fractions.Fraction((10**i),n)) != fractions.Fraction(1,n) and i < 1000:
            i += 1
        return i
    elif n in range(101,1001):
        i = 3
        while  fractions.Fraction((10**i), n) - int(fractions.Fraction((10**i),n)) != fractions.Fraction(1,n) and i < 1000:
            i += 1
        return i         
a = [num(n) for n in range(11,1001)]
uwu = 0
for i in a:
    if i != 1000 and i > uwu:
        uwu = i
print('El más grande es de longitud: ', uwu)
print('El número que lo da es: ', a.index(uwu)+1+10)
print("--- %s seconds ---" % (time.time() - start_time))