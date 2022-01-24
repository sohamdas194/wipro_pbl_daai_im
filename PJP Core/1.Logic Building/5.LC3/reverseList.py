# Design an algorithm to accept 10 integer elements for an array and then rearrange the elements in the array in reverse order. The reversed array must be displayed as output.

if __name__ == '__main__':
	numbers = []

	print("Enter numbers one by one:")

	for i in range(10):
		numbers.append(int(input()))
	
	for i in range(int(10/2)):
		temp = numbers[i]
		numbers[i] = numbers[9-i]
		numbers[9-i] = temp

	print("Reversed list:", numbers)
