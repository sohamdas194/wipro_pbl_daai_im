file1 = open('./text_file_lorem.txt', 'r')
user_word = input("Enter the word whose frequency you want to find out in text_file_lorem: ").lower()

count = 0
lines = file1.readlines()

for line in lines:
	words = line.split()
	for word in words:
		if word.lower() == user_word:
			count += 1

print("frequency of %s in text_file_lorem.txt is: %d" %(user_word, count))

file1.close()
