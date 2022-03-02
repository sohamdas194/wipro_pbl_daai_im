# MyList1 = [10,20,10,40,50,60]
# MyList1.reverse()
# print(MyList1)


MyList1 = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    MyList1.append(ele)
 
print("The elements of list are: ")
print(MyList1)
MyList1.append(60)
MyList1.reverse()
print()
print("Reverse of list is: ", MyList1)
print()