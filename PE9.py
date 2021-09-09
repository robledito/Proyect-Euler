print('Terna pitagorica cuya suma es 1000, y su producto es:')
for n in range(0,1001):
    for m in range(0,1001):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a + b + c == 1000 and a*b*c > 0:
            print(a*b*c)
