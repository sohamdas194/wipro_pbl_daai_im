# Design an algorithm which accepts a set of N (consider N to be 30) student's examination marks (in the range of 0 to 100). Then make a count of the number of students that obtain each possible marks(i.e. count of how many students scored 0, count of how many students scored 1, ..... till count of how many students scored 100)

if __name__ == '__main__':
	numbers = []
	marksFreq = list()
	
	# initializing every list element with 0
	for i in range(101):
		marksFreq.append(0)

	N = int(input("Enter number to students: "))

	print("Enter student's examination marks one by one:")

	for i in range(N):
		while True:
			x = int(input())
			if x>=0 and x<=100:
				break
			else:
				print("Only enter marks in the range of 0 to 100.\nTry again...\n")
		numbers.append(x)

	for i in numbers:
		marksFreq[i] += 1

	print("Mark \t\t Frequency")
	print("-----------------------------")
	for i in range(101):
		print(f"{i} \t\t {marksFreq[i]}")
