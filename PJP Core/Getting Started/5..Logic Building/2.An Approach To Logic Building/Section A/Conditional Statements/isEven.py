# Write a program to accept a number N and print whether the is EVEN or ODD.

def isEven(N):
	if N & 1:
		return False
	else:
		return True

if __name__ == '__main__':
	print("Is even:", isEven(int(input("Enter a number: "))))
