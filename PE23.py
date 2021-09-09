import math, time
a = set()
def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
                if total > n:
                    a.add(n)
for uwu in range(2,28124):
    sum_div(uwu)
a = list(a)
b = list(range(1,28124))
for j in a:
    for i in a:
        if ((i + j) < 28124) and (i + j) in b:
            b.remove((i+j))
print(sum(b))