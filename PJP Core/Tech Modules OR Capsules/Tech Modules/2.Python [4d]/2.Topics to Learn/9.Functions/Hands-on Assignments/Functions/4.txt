def printNumberOfUpperAndLowerCaseLetters(MyString):
	upper = lower = 0

	for ch in MyString:
		if ch.islower():
			lower += 1
		elif ch.isupper():
			upper += 1

	print('Number of lower case letters in: ', lower)
	print('Number of upper case letters in: ', upper)

printNumberOfUpperAndLowerCaseLetters("WIPRO Tech.")
