a = str(2**1000)
numli = []
for i in range(0, len(a)):
    numli.append(int(a[i]))
suma = 0
for num in numli:
    suma = suma + num

print(suma)