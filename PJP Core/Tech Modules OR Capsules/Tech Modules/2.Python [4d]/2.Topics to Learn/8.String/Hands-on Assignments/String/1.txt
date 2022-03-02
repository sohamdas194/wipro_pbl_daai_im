MyString = "A b 3 C D 4 e F j"
upper = lower = 0

for ch in MyString:
	if ch.islower():
		lower += 1
	elif ch.isupper():
		upper += 1

print('Number of lower case letters in MyString: ', lower)
print('Number of upper case letters in MyString: ', upper)
