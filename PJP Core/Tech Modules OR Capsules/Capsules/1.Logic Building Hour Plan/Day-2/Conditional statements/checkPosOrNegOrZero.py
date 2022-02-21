# WAP to accept a number N and print whether it is positive, negative or zero

def main():
	N = int(input("Enter a number: "))

	if N < 0:
		print("Negative Number")
	elif N > 0:
		print("Positive Number")
	else:
		print("Zero")


if __name__ == '__main__':
	main()
