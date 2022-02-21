# Design an algorithm which accepts a binary representation of a number and then displays its corresponding decimal equivalent.

def binaryToDecimal(bn):
	num = 0
	for b in bn:
		num <<= 1
		if(b == '1'):
			num |= 1
	return num

if __name__ == '__main__':
	bn = input('Enter the binary number: ')

	print(binaryToDecimal(bn))
