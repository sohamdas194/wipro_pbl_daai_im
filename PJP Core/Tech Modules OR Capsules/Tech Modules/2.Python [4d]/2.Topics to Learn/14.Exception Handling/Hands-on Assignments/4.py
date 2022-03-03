num_list = [-10, 20, -30, -40, 50, 60, -70, 80, -90, 100]

index = int(input("Enter the index: "))

try:
	num = num_list[index]
except IndexError:
	print("Entered index in invalid!!")
else:
	if num < 0:
		print("Number is negative")
	elif num > 0:
		print("Number is positive")
	else:
		print("Number is zero")
