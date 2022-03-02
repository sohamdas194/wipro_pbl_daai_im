inputStr = input("Enter a string: ")

newStr = inputStr[1:-1]

if inputStr[0] != 'x':
	newStr = inputStr[0] + newStr
if inputStr[-1] != 'x':
	newStr = newStr + inputStr[-1]

print(newStr)
