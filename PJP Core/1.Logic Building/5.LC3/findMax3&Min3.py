# Design an algorithm to accept 20 integer elements for an array and print the maximum 3 and minimum 3 elements from the array.
# Note: Sorting of array elements are not expected as part of this activity.

if __name__ == '__main__':
	numbers = []

	print("Enter numbers one by one:")

	for i in range(20):
		numbers.append(int(input()))

	min1 = min2 = min3 = max(numbers)
	max1 = max2 = max3 = min(numbers)

	for i in numbers:
		if min1 > i:
			if min2 > i:
				if min3 > i:
					min1 = min2
					min2 = min3
					min3 = i
					continue
				min1 = min2
				min2 = i
				continue
			min1 = i
			continue

	for i in numbers:
		if max1 < i:
			if max2 < i:
				if max3 < i:
					max1 = max2
					max2 = max3
					max3 = i
					continue
				max1 = max2
				max2 = i
				continue
			max1 = i
			continue
		
	print("Minimum 3 numbers in the list: " + str(min1) + ", " + str(min2) + ", " + str(min3))
	print("Maximum 3 numbers in the list: " + str(max1) + ", " + str(max2) + ", " + str(max3))
