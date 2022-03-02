# MyList1 = [10,20,10,40,50]
# print(MyList1)
# print(MyList1[2]) #printing 3rd element
# print(MyList1[4]) #printing 4th element
# print()
# MyList1.append(60) #adding an element
# print("List after adding element")
# print(MyList1)


MyList1 = []
n = int(input("Enter the number of elements in the list: "))

print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    MyList1.append(ele)
 
print("The elements of list are: ")
print(MyList1)
print()

MyList1.append(60)

print("List after adding an element")
print(MyList1)