MyList1 = [60, 50, 10, 40, 20, 10]
MyList2 = [11, 21]

for i in range(len(MyList2)):
	MyList1.insert(i, MyList2[i])

print('MyList1 after appending Mylist2 in the front:\n', MyList1)
