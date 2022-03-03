file1 = open('./text_file_append.txt', 'a')
new_content = input("Enter what you want to append to text_file_append.txt: ")

file1.write(new_content)
file1.write('\n')

file1.close()
