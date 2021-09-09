import time

def palin(n):
    numero = str(n)
    for i in range(int(len(numero)/2)+1):
        if numero[i] != numero[-i-1]:
            return False
            break
    return True

start_time = time.time()
deci = {x for x in range(1,1000001,2) if palin(x) == True}
bina = {x for x in deci if palin(format(x,'b')) == True}

print("La suma de palindromos binarios y decimales es: {}".format(sum(deci.intersection(bina))))
print("--- %s seconds ---" % (time.time() - start_time))