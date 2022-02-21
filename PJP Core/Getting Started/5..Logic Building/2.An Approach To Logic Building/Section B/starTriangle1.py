# Write a program to print:
#                   *
#                 * *
#               * * *
#             * * * *
#           * * * * *
#         * * * * * *
#       * * * * * * *
#     * * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * *

if __name__ == '__main__':
	for row in range(10):
		for space in range(9-row):
			print("  ", end = '')

		for stars in range(row+1):
			print("* ", end = '')

		print()
