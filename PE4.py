def getPalindrome(lower, upper):             # Función que obtiene palíndromos
  listPalind = []
  for n in range(lower, upper):
    if str(n) == str(n)[::-1]:
      listPalind.append(int(n))
  return listPalind

a = getPalindrome(10000,1000000)

listaFactor = []

def Factor(n):
    for i in range(100,1000):
        if n % i == 0 and n // i < 1000:
            listaFactor.append(n)
            print('Los números que descomponen a %s son %s y %s' % (n, i, n // i))
            
for num in a:
    Factor(num)
    
print(listaFactor[-1])