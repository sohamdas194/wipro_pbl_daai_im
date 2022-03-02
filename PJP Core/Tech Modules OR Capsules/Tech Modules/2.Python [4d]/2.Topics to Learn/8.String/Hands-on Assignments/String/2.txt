MyString = 'Racecar'
MyString = MyString.lower()
MyStringRev = (MyString)[::-1]

if MyString == MyStringRev:
	print("%s is palindrome" %(MyString))
else:
	print("%s is not palindrome" %(MyString))
