num = int(input("Enter a number: "))
temp = num
sum = 0
while temp != 0:
	sum += temp%10
	temp //= 10
print("Sum of digits of %d is %d" %(num, sum))
