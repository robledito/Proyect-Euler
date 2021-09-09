def conse(a,b):
    i = 0
    while (i**2 + i*a + b) in prim:
        i += 1
    return i
# print(max(a,key=lambda item:item[0]))
print('La n-ada que lo resuleve es: (71, -61, 971)')
print('El producto es: ', -61*971)