# WAP to read 10 integers from the user to find their average and also find out how many integers are less than the average.

if __name__ == '__main__':
	sum = 0
	numbers = []
	count = 0
	average = 0.0

	print("Enter numbers one by one:")

	for i in range(10):
		numbers.append(int(input()))
		sum += numbers[i]

	average = sum / 10

	for i in range(10):
		if numbers[i] < average:
			count += 1

	print("Average:", average)		
	print("Count:", count)
