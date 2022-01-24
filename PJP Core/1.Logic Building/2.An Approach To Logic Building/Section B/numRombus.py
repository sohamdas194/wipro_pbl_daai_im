# Write a program to print:
#          1
#         121
#        12321
#       1234321
#      123454321
#     12345654321
#    1234567654321
#   123456787654321
#  12345678987654321
# 12345678910987654321
#  12345678987654321
#   123456787654321
#    1234567654321
#     12345654321
#      123454321
#       1234321
#        12321
#         121
#          1

if __name__ == '__main__':
	for row in range(1, 11):
		for space in range(10-row):
			print(' ', end='')

		for incr in range(1, row+1):
			print(incr, end='')

		for dcr in range(row-1, 0, -1):
			print(dcr, end='')

		print()

	for row in range(9, 0, -1):
		for space in range(10-row):
			print(' ', end='')

		for incr in range(1, row+1):
			print(incr, end='')

		for dcr in range(row-1, 0, -1):
			print(dcr, end='')

		print()