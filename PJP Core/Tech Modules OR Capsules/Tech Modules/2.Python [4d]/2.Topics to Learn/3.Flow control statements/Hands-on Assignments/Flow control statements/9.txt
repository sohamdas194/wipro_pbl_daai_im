num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp != 0:
	reverse = reverse*10 + temp%10
	temp //= 10
print("Reverse of %d is %d" %(num, reverse))
