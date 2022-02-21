# Design an alogrithm which accepts a number from the user and displays its smallest exact divisor other than one

def findSmallestExactDivisor(n):
	if n<=1:
		return n
	for i in range(2, n+1):
		if n%i == 0:
			return i

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	print("Smallest exact divisor:", findSmallestExactDivisor(n))
