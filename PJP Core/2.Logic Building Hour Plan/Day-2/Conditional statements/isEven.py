# WAP to accept a number N and print whether the number is EVEN or ODD

def isEven(N):
	if N%2 == 0:
		return True
	else:
		return False

def main():
	N = int(input("Enter a number: "))

	if isEven(N):
		print("Even Number")
	else:
		print("Odd Number")

if __name__ == '__main__':
	main()
