# Sum of last digit of two given numbers
# Rohit wants to add the last digits of two given numbers.
# For example,
# If the given numbers are 287 and 154, the output should be 11.
# Below is the explanation -
# Last digit of the 267 is 7 
# Last digit of the 154 is 4 
# Sum of 7 and 4 = 11

# Write a program to help Rohit achieve this for any given two numbers.
# The prototype of the method should be -

# int addLastDigits(int input1, int input2);
# where input1 and input2 denote the two numbers whose last digits are to be added.

# Note: The sign of the input numbers should be ignored.
# i.e.
# if the input numbers are 267 and 154, the sum of last two digits should be 11
# if the input numbers are 267 and -154, the sum of last two digits should be 11
# if the input numbers are -267 and 154, the sum of last two digits should be 11
# if the input numbers are -267 and -154, the sum of last two digits should be 11

def addLastDigits(input1, input2):
	from getLastDigit import getLastDigit

	return getLastDigit(input1) + getLastDigit(input2)

def main():
	x = int(input("Enter a number: "))
	y = int(input("Enter a number: "))

	print(addLastDigits(x, y))

if __name__ == '__main__':
	main()

