# Design an algorithm which accepts a decimal integer and then displays its corresponding binary representation.

def intToBinary(n):
	if n == 0:
		print(0, end='')
		return

	intToBinary(n>>1)
	print((n & 1), end='')

if __name__ == '__main__':
	n = int(input("Enter a number: "))

	intToBinary(n)
