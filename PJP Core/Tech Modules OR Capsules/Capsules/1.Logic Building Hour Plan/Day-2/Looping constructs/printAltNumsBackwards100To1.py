# WAP to print numbers backwards from 100 to 1 by skipping 2 numbers i.e. 100 97 94 91 88 85 82 79 ... 22 19 16 13 10 7 4 1

def main():
	i = 100
	while i >= 1:
		print(i)
		i -= 3

if __name__ == '__main__':
	main()
