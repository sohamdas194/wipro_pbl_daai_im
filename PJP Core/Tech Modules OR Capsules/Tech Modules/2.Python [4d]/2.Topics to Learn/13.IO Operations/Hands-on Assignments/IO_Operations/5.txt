file1 = open('./text_file_lorem.txt', 'r')

longestWord = ''

lines = file1.readlines()
for line in lines:
	words = line.split()
	for word in words:
		if len(word) > len(longestWord):
			longestWord = word

print("Longest Word in the file text_file_lorem.txt: ", longestWord)

file1.close()
