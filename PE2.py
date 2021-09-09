# Fibonacci hasta el número n (suma de pares)
n = int(input('Valor: '))
def Fbn(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fbn(n-2) + Fbn(n-1)
listaFbn = []
for i in range(1,n+1):
    listaFbn.append(Fbn(i))
A = [b for b in listaFbn if b % 2 == 0]

def sumalista(A):
    suma = 0
    for i in A:
        suma = suma + i
    return suma
print(sumalista(A))