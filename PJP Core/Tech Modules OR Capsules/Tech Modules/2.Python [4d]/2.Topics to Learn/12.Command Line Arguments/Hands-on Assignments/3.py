from sys import argv
import math

def isPrime(num):
	if num <= 1:
		return False
	for i in range(2, int(math.sqrt(num))+1):
		if num%i == 0:
			return False
	return True

n = len(argv)
if n != 11:
	print("Please pass 10 numbers!!")
	exit(1)

sum = 0	
for i in range(1, len(argv)):
	num = int(argv[i])
	if isPrime(num):
		sum += num

print("Sum of prime numbers among the passed 10 numbers: ", sum)
