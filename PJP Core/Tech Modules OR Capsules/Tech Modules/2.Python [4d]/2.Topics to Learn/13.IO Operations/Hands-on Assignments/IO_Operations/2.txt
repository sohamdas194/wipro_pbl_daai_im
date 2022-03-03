file1 = open('./text_file_alpha.txt', 'r')
n = int(input("Enter the number of lines to print from text_file_alpha.txt: "))

line = file1.readline()

print("Contents of the file:")
print("~~~~~~~~~~~~~~~~~~~~~")
while line != '' and n != 0:
	print(line, end='')
	line = file1.readline()
	n -= 1

file1.close()
