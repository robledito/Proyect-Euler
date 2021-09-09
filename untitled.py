def D(n): 
    if n==0: 
        return 400000*1.05
    else: 
        return ((D(n-1)*1.05 )) - 25000
print(D(37))