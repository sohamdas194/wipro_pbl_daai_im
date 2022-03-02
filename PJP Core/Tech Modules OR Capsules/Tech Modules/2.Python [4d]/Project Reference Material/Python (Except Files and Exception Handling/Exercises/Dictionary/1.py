# Mydic1 = {0:10, 1:20}
# Mydic1.update({2:30})
# print(Mydic1)\

Mydic1 = {0:10, 1:20}
key = int(input("Enter a key value: "))
value = int(input("Enter the value for the key: "))

Mydic1.update({key:value})

print(Mydic1)