a = int(input('Cota inferior '))
b = int(input('Cota superior '))
inter = [num for num in range(a, b+1)]
multi = []
n = 0

while n < 100000000000:
    n += 1
    if all(inter[-1]*n % inter[i] == 0 for i in range(0,len(inter))):
        multi.append(max(inter)*n)
        break

print('El mínimo común múltiplo es: ', inter[-1]*n)