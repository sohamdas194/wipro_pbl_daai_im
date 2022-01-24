# Design an algorithm which accepts 2 strings from the user and performs the following operations on it.

# Example-
# 	string1 = "Hello"
# 	string2 = "World"
# 	string3 must be "HellodlroW"

# Both strings must be concatenated but afte reversing the second string (as shown in string3 above).

from reverseStr import *

def reverseAndConcat(inputstr1, inputstr2):
	reveredInputstr2 = reverseStr(inputstr2)
	return inputstr1 + reveredInputstr2

def main():
	inputstr1 = input("Enter the first string: ")
	inputstr2 = input("Enter the second string: ")

	result = reverseAndConcat(inputstr1, inputstr2)

	print("Resultant string:", result)

if __name__ == '__main__':
	main()
