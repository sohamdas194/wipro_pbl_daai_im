file_name = input("Enter the file path: ")
try:
	file1 = open(file_name, 'r')
except FileNotFoundError:
	msg = "Sorry, the file " + file_name + " doesn't exist."
	print(msg)
else:
	lines = file1.readlines()

	print("Contents of the file:")
	print("~~~~~~~~~~~~~~~~~~~~~")
	for line in lines:
		print(line)
