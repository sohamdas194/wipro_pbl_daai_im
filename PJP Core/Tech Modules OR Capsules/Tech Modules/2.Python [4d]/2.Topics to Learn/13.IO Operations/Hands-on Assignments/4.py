file1 = open('./text_file_alpha.txt', 'r')

# lines = file1.readlines()

lines = []
line = file1.readline()

while line != '':
	lines.append(line)
	line = file1.readline()

print("List:\n", lines)

file1.close()
