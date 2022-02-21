# Design an algorithm that accepts a number and displays each digit of the number separetely.

def printDigitsInANumber(n):
	while(n != 0):
		x = n%10
		print(x, end=' ')
		n = int(n/10)
	print()

def printDigitsInANumberV2(n):
	if n == 0:
		return
	printDigitsInANumberV2(int(n/10))
	print(n%10, end=' ')

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	printDigitsInANumber(n)
	printDigitsInANumberV2(n)
	print()
	

