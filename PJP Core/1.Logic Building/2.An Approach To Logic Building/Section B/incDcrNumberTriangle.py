# Write a program to print:
#                   1
#                 1 2 1
#               1 2 3 2 1
#             1 2 3 4 3 2 1
#           1 2 3 4 5 4 3 2 1
#         1 2 3 4 5 6 5 4 3 2 1
#       1 2 3 4 5 6 7 6 5 4 3 2 1
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1

if __name__ == '__main__':
	for row in range(1, 11):
		for space in range(10-row):
			print(' ', end=' ')

		for incr in range(1, row+1):
			print(incr, end=' ')

		for dcr in range(row-1, 0, -1):
			print(dcr, end=' ')

		print()
