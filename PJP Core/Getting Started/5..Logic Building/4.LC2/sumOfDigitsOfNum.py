# Design an alogrithm to find the sum of all the digits ina given number.

def sumOfDigitsInNum(n):
	sum = 0
	while n != 0:
		sum+=n%10
		n = int(n/10)
	return sum

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	print("Sum of digits:", sumOfDigitsInNum(n))
