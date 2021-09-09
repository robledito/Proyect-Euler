# Suma de los múltiplos de 3 y 5 hasta un número a
a = int(input('Échame una épsilon: '))
lista = list(range(3,a))
divisor3_5 = []
for number in lista:
    if number % 3 == 0 or number % 5 == 0:
        divisor3_5.append(number)

def sumalista(divisor3_5):
    suma = 0
    for i in divisor3_5:
        suma = suma + i
    return suma

print(sumalista(divisor3_5))