# Design an algorithm to accept a string from the user. Count and print the number of times each character occurs in the given string.
# Example-
# 	input string = "malayalam"
# 	Output must be-
# 	m - 2
# 	a - 4
# 	l - 2
# 	y - 1

def printCountOfOccuringChars(inputstr):
	countOfOccuringChars = {}

	for ch in inputstr:
		if ch in countOfOccuringChars:
			countOfOccuringChars[ch] += 1
		else:
			countOfOccuringChars[ch] = 1

	print("Char \t\t Occurence")
	print("----------------------------")
	for key in countOfOccuringChars:
		print(f"{key} \t\t {countOfOccuringChars[key]}")


def main():
	inputstr = input("Enter a string: ")

	printCountOfOccuringChars(inputstr)

if __name__ == '__main__':
	main()
