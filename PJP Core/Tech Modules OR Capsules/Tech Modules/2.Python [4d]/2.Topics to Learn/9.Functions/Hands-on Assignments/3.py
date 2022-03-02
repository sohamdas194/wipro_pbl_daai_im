def getFactorial(num):
	if num < 0: 
		return None 
	if num == 0:
		return 1

	return num * getFactorial(num-1)

print("Factorial of 5: ", getFactorial(5))
