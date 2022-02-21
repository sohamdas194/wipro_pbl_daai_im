# WAP to accept two numbers and print the greater value of the two.

def main():
	x = int(input("Enter the first number: "))
	y = int(input("Enter the second number: "))


	print("Greater number between the inputed numbers is:")
	if x > y:
		print(x)
	else:
		print(y)


if __name__ == '__main__':
	main()
