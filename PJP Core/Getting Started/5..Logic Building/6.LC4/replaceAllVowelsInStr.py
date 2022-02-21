# Design an algorithm to accept a string from the user. Replace all vowels ('a', 'e', 'i', 'o', 'u') with 'z'. If there are no vowels in the string just print the original word with the message "No vowels present".

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

def replaceVowelsInStr(inputstr):
	replaceFlag = False
	chToReplaceWith = 'z'
	vowels = ['a', 'e', 'i', 'o', 'u']
	strList = strToList(inputstr)
	for i in range(len(strList)):
		for vowel in vowels:
			if strList[i].lower() == vowel:
				if not replaceFlag:
					replaceFlag = True
				strList[i] = chToReplaceWith

	if replaceFlag:
		print("New String: " + listToStr(strList))
	else:
		print("No vowels present in " + inputstr)

def main():
	inputstr = input("Enter a string: ")

	replaceVowelsInStr(inputstr)

if __name__ == '__main__':
	main()
