# Design an alogrithm that reads a list of 5 numbers (both +ve and -ve) make makes a count of the number of negative and non-negative numbers in the list.
# Note: 0 must be considered as a +ve number in this algorithm

if __name__ == '__main__':
	# n = int(input("Enter the number of elements you want to enter: "))
	n = 5

	nums = []

	print("Enter the numbers one by one: ")
	for i in range(n):
		nums.append(int(input()))

	posCount = 0
	negCount = 0

	for x in nums:
		if x >= 0:
			posCount += 1

		else:
			negCount += 1

	print("Number of +ve number:", posCount)
	print("Number of -ve number:", negCount)
