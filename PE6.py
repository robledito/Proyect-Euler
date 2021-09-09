n = int(input('¿Hasta que número?'))
def sumas(n):
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
    return suma**2

def cuadrados(n):
    cuad = 0
    for i in range(1,n+1):
        cuad = cuad + i**2
    return cuad


print(-(cuadrados(n) - sumas(n)))

