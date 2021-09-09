def p(n):
    return n*(3*n-1)/2
def h(n):
    return n*(2*n-1)
iguales = []
for a in range(20000,30000):
    for n in range(30000, 40000):
        if h(a) == p(n):
            iguales.append(h(a))
print(iguales)
    