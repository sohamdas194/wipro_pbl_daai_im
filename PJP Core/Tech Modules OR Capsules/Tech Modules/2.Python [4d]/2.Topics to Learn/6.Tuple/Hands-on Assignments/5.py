Mylist = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]

for i in range(len(Mylist)):
	subTuple = Mylist[i]
	
	tempList = list(subTuple)
	tempList[len(tempList) - 1] = 100

	Mylist[i] = tuple(tempList)

print(Mylist)
