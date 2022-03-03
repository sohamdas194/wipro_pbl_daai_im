num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp != 0:
	reverse = reverse*10 + temp%10
	temp //= 10
if num == reverse:
	print("%d is a palindrome" %(num))
else:
	print("%d is not a palindrome" %(num))
