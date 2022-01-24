# Program to swap two numbers

if __name__ == '__main__':
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	b = a*b
	a = int(b/a)
	b = int(b/a)
	print("After swapping:")
	print("a: ", a)
	print("b: ", b)
