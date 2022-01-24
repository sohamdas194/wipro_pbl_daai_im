#program to swap 3 numbers 

# b = a
# c = b 
# a = c

if __name__ == '__main__':
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	temp = a 
	a = c 
	c = b
	b = temp
	print("After swapping:")
	print("a: ", a)
	print("b: ", b)
	print("c: ", c)
