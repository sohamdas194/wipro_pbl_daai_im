from math import sqrt

num = int(input("Enter a number: "))
if num<2:
	print("Number is not prime")
	exit()
for i in range(2, int(sqrt(num))+1):
	if num%i == 0:
		print("Number is not prime")
		exit()
print("Number is prime")
