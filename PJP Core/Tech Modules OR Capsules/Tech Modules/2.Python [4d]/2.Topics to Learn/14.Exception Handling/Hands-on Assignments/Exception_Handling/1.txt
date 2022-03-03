try:
	x = float(input("Enter the first number: "))
	y = float(input("Enter the second number: "))

	res = x/y

except:
	print("Exception occured")

else:
	print("Result: ", res)
