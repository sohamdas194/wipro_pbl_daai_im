from sys import argv

n = len(argv)
if n != 3:
	print("Please pass 2 numbers!!")
	exit(1)

sum = 0

for i in range(1, n):
	sum += int(argv[i])

print("Sum: ", sum)
