def printEvenNumbersInList(MyList):
	for x in MyList:
		if x%2 == 0:
			print(x, end=' ')

MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
printEvenNumbersInList(MyList)
