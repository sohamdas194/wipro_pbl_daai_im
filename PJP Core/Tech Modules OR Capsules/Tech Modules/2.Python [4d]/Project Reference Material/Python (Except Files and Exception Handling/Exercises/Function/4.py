def lower1(a):
    lo = 0
    up = 0
    for i in a:
        if i.islower():
            lo +=1
        if i.isupper():
            up +=1
                
     

    print("The number of lowercase characters:", lo)
    print("The number of uppercase characters:", up)


lower1("TeST123")