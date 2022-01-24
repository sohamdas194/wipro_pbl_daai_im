# Write a program to print:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10

if __name__ == '__main__':
	for row in range(1, 11):
		for num in range(1, row+1):
			print(num, end = ' ')
		print()
