file1 = open('./text_file_alpha.txt', 'r')

line = file1.readline()

print("Contents of the file:")
print("~~~~~~~~~~~~~~~~~~~~~")
while line != '':
	print(line, end='')
	line = file1.readline()

file1.close()
