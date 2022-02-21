# Write a program to accept two numbers and print whether their sum is EVEN or ODD.

from isEven import isEven

def isSumEven(a, b):
	sum = a + b
	return isEven(sum)

if __name__ == '__main__':
	a = int(input("Enter a number: "))
	b = int(input("Enter another number: "))
	print("Is sum even:", isSumEven(a, b))
