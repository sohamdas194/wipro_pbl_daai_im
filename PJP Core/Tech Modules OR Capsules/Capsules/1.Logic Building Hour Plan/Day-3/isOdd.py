# Is Odd?
# Write a function to find whether the given input number is Odd. 
# If the given number is odd, the fucntion should return 2 else it should return 1.
# Note: The number passed to the fucntion can be negative, positive or zero.
# Zero should be treated as Even.

def isOdd(N):
	if N%2 != 0:
		return 2
	else:
		return 1

def main():
	N = int(input("Enter a number: "))

	if isOdd(N) != 2:
		print("Not Odd")
	else:
		print("Odd")

if __name__ == '__main__':
	main()
