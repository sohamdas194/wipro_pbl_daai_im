# Design an algorithm to accept 2 strings (string1 and string2) from the user. Concatenate both the strings into a thired string "string3" and print the result.
# Example-
# 	string1 = "Hello"
# 	string3 = "World"
# 	string3 must be "HelloWorld"

def concat(string1, string2):
	result = ""
	for ch in string1:
		result += ch
	for ch in string2:
		result += ch
	return result


def main():
	inputstr1 = input("Enter the first string: ")
	inputstr2 = input("Enter the second string: ")

	result = concat(inputstr1, inputstr2)

	print("Concatinated string:", result)

if __name__ == '__main__':
	main()
