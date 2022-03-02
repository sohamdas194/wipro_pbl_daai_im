st = input("Enter a string: ")

up = 0
lo = 0

for i in st:
    if (i.islower()):
        lo += 1
    else:
        up += 1

print("The number of lowercase characters: ", lo)
print("The number of uppercase characters: ", up)