inputStr = input("Enter a string: ")
n = int(input("Enter n: "))
newStr = ''
for i in range(n):
	newStr += inputStr[-n:]
print(newStr)
