# Given a set of 3 numbers, design an algorithm that adds these numbers and returns the resultant sum

if __name__ == '__main__':
	n = 3
	# n = int(input("Enter the number of elements you want to enter: "))

	num = []

	print("Enter the numbers one by one:")
	for x in range(n):
		num.append(int(input()))

	sum = 0
	for x in num:
		sum += x

	print("Resultant sum:", sum)
