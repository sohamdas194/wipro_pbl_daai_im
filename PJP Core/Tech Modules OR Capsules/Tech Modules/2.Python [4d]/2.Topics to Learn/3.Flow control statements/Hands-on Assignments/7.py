def isPrime(num):
	from math import sqrt

	if num<2:
		return False
	for i in range(2, int(sqrt(num))+1):
		if num%i == 0:
			return False
	return True

print("Prime numbers between 10 and 99:")
for i in range(10, 100):
	if isPrime(i):
		print(i)
