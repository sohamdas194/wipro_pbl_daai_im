while True:
	inputStr = input("Enter a string: ")
	if len(inputStr) >= 2:
		break
	else:
		print("Enter string is too short, it's lenght should be >= 2")

for i in range(len(inputStr)):
	print(inputStr[:2], end='')
