# Return second last digit of the given number
# Write a function that returns the second last digit of the given number.
# Second last digit is being referred to the digit in the tens place in the given number.
# for example,
# if the given number is 197, the last digit is 9

# Note1 - The second last digit should be returned as a positive number.
# i.e. if the given number is -197, the last digit is 9

# Note2 - If the given number is a single digit number, then the second last digit does not exist.
# In such cases, the function should return -1 
# i.e. if the given number is 5, the second last digit should be returned as -1

def getSecondLastDigit(N):
	res = int((abs(N) % 100)/10)
	if res == 0:
		return -1 
	else:
		return res 

def main():
	N = int(input("Enter a number: "))

	print(getSecondLastDigit(N))

if __name__ == '__main__':
	main()
