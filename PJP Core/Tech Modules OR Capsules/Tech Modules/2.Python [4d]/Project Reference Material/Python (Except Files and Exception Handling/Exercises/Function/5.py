def even(list1):
    eve= []
    for i in list1:
        if i % 2 == 0:
            eve.append(i)
    return eve

li = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

print(even(li))