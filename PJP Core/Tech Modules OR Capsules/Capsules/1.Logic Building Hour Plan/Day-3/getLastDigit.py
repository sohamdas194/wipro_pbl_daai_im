# Return last digit of the given number
# Write a function that returns the last digit of the given number.
# Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.
# for example,
# if the given number is 197, the last digit is 7
# if the given number is -197, the last digit is 7

def getLastDigit(N):
	return abs(N) % 10

def main():
	N = int(input("Enter a number: "))

	print(getLastDigit(N))

if __name__ == '__main__':
	main()
