dic = {1:10, 2:20, 3:30}

print("printing only keys")
for i in dic:
    print(i, end="  ")
    
print()
print("printing only values")
for i in dic:
    print(dic[i], end = "   ")
    
print()
print("printing keys and values")
for i in dic:
    print(i, end = "    ")
    print(dic[i], end = "   ")