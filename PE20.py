n = int(input('Numero '))
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

a = str(fact(n))
numli = []
for i in range(0, len(a)):
    numli.append(int(a[i]))
suma = 0
for num in numli:
    suma = suma + num
print(suma)