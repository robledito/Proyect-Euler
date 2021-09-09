def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a

n = 12
while fib(n) - 10**999 < 0:
    n += 1
    if fib(n) - 10**999 > 0:
        break
print(n)