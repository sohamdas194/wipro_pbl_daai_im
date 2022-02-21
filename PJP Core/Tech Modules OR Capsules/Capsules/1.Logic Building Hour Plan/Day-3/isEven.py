# Is Even ?
# Write a function to find whether the given input number is Even.
# If the given number is even, the function should return 2 else it should return 1.
# Note: The number passed to the function can be negative, positive or zero.
# Zero should be treated as Even.

def isEven(N):
	if N%2 == 0:
		return 2
	else:
		return 1

def main():
	N = int(input("Enter a number: "))

	if isEven(N) == 2:
		print("Even")
	else:
		print("Not Even")

if __name__ == '__main__':
	main()

