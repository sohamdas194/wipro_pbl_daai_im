def fact(a):
    fac = 1
    for i in range(1,a+1):
        fac = fac * i
    
    return fac

print(fact(5))