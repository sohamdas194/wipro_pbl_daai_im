# Design an algorithm to accept 10 integer elements for an array and print the sum of all the elements.

if __name__ == '__main__':
	sum = 0
	numbers = []

	print("Enter numbers one by one:")

	for i in range(10):
		numbers.append(int(input()))
		sum += numbers[i]

	print("Sum:", sum)
	