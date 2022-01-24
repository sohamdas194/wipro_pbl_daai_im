# Design an algorithm to count the number of digits in a given number.

def countDigitsInANumber(n):
	count = 0
	while n != 0:
		n = int(n/10)
		count+=1
	return count

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	print("Digits:", countDigitsInANumber(n))
