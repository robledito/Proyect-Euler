n = int(input('Número: '))
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1
print('El factor primo más grande es',n)