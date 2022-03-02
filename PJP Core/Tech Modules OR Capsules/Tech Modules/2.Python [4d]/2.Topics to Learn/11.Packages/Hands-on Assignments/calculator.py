import math_package as m

print("~~~~~~Calculator~~~~~~")

while True:
	print("\nEnter 1: To Add")
	print("Enter 2: To Subtract")
	print("Enter 3: To Multiply")
	print("Enter 4: To Divide")
	print("Enter 0: To Exit\n")
	choice = input("Enter you choice:")

	if choice == '1':
		x = int(input("\nEnter the first number: "))
		y = int(input("Enter the second number: "))
		print("Addition Result: ", m.math_module.add(x, y))
	elif choice == '2':
		x = int(input("\nEnter the first number: "))
		y = int(input("Enter the second number: "))
		print("Addition Result: ", m.math_module.sub(x, y))
	elif choice == '3':
		x = int(input("\nEnter the first number: "))
		y = int(input("Enter the second number: "))
		print("Addition Result: ", m.math_module.mul(x, y))
	elif choice == '4':
		x = int(input("\nEnter the first number: "))
		y = int(input("Enter the second number: "))
		print("Addition Result: ", m.math_module.div(x, y))
	elif choice == '0':
		break
	else:
		print("Invalid input!! Try again")
