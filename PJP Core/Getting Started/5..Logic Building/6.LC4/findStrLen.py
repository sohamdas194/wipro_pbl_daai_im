# Design an algorithm to accept a string from the user and calculate its length.

def strlen(inputstr):
	length = 0

	try:
		while True:
			if inputstr[length] != '':
				length += 1		
	except Exception as e:
		#print("Exception caught:", e)
		return length

def main():
	inputstr = input("Enter a string: ")

	print("Length of the string is:", strlen(inputstr))

if __name__ == '__main__':
	main()
