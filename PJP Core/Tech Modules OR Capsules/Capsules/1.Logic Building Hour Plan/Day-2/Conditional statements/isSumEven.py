# WAP to accept two numbers and print whether their sum is EVEN or ODD.

def main():
	x = int(input("Enter the first number: "))
	y = int(input("Enter the second number: "))


	from isEven import isEven

	if isEven(x + y):
		print("Sum is Even")
	else:
		print("Sum is Odd")


if __name__ == '__main__':
	main()
