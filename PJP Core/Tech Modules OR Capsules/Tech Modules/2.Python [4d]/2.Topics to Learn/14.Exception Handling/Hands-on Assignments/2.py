import math

def isPrime(num):
	if num <= 1:
		return False
	for i in range(2, int(math.sqrt(num))+1):
		if num%i == 0:
			return False
	return True

while True:
	try:
		num = int(input("Enter a number: "))
	except:
		print("Error occured!! entered value is not a number")
		print("Please, try again")
	else:
		break

if isPrime(num):
	print(f"{num} is prime")
else:
	print(f"{num} is not prime")
