# Write a program to print: 
#                   1
#                 1 2 A
#               1 2 3 B A
#             1 2 3 4 C B A
#           1 2 3 4 5 D C B A
#         1 2 3 4 5 6 E D C B A
#       1 2 3 4 5 6 7 F E D C B A
#     1 2 3 4 5 6 7 8 G F E D C B A
#   1 2 3 4 5 6 7 8 9 H G F E D C B A
# 1 2 3 4 5 6 7 8 9 10 I H G F E D C B A

if __name__ == '__main__':
	for row in range(1, 11):
		for space in range(10-row):
			print(' ', end=' ')

		for num in range(1, row+1):
			print(num, end=' ')

		for alpha in range(63+row, 64, -1):
			print(chr(alpha), end=' ')

		print()	
