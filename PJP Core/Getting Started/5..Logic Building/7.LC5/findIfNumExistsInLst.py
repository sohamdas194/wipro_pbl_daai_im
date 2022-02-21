# Design an algorithm to find the position of a number X (entered by user and if it occurs) in an array of 15 elements. Array elements are also entered by the user.

def findNumIndex(lst, num):
	for i in range(len(lst)):
		if lst[i] == num:
			return i
	return -1

def main():
	lst = []

	# n = int(input("Enter size of the list:"))
	n = 5
	print("Enter 25 elements in the first list one by one:")
	for i in range(n):
		lst.append(int(input()))

	num = int(input("Enter the number to find: "))
	result = findNumIndex(lst, num)

	if result == -1:
		print("Element not in the list")
	else:
		print("Element found at pos:", result)

if __name__ == '__main__':
	main()

