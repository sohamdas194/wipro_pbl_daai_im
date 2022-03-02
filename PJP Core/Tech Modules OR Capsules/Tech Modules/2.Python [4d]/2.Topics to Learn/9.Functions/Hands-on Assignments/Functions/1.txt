def sumList(MyList):
	sum = 0
	for x in MyList:
		sum += x
	return sum

MyList = [8, 2, 3, 0, 7]
print("Sum of elements of MyList: ", sumList(MyList))
