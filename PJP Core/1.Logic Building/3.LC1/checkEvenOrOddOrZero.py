# Design an algorithm that reads a number from the user and tells if it is even or odd or a zero.

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	if n == 0:
		print("Zero")
	elif n%2 == 0:
		print("Even")
	else:
		print("Odd")
