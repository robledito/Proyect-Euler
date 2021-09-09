#n = int(input('Número '))

def collatz(n):
    iteracion = 0
    while n != 1:
        iteracion = iteracion + 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n +1
    return iteracion

lista = []

for a in range(1, 1000000):
    lista.append(collatz(a))

print(lista.index(524))