from sys import argv

n = len(argv)
if n != 2:
	print("Please pass a single message!!")
	exit(1)

print("File name: ", n)
for i in range(1, len(argv)):
	print("Welcome message: ", argv[i])
