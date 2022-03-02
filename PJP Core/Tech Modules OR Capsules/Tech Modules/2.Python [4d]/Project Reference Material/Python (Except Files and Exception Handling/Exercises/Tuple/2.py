tup = (1, 2, 3, 4)

print(tup)

ele = int(input("Enter the element to be searched: "))

if ele in tup:
    print("Element exists in tuple")
else:
    print("Element doesn't exist in tuple")