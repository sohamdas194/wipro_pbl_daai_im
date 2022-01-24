# Design an algorithm to accept a string from the user. Reverse the string and display it.

def strToList(inputstr):
	strList = []
	for ch in inputstr:
		strList.append(ch)
	return strList

def  listToStr(inputlst):
	listStr = ''
	for x in inputlst:
		listStr += x
	return listStr

def reverseStr(inputstr):
	strList = strToList(inputstr)
	n = len(strList) - 1
	for i in range(int(n/2)+1):
		temp = strList[i]
		strList[i] = strList[n-i]
		strList[n-i] = temp
	return listToStr(strList)

def main():
	inputstr = input("Enter a string: ")

	reversedStr = reverseStr(inputstr)

	print("Reversed string:", reversedStr)

if __name__ == '__main__':
	main()
