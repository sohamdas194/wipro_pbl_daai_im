# Modify the algorithm written in Activity 4 in order to get count of students in a specific range of marks as defined below.
# Range of marks:
# ---------------
# 0     to   10%
# 11%   to   20%
# .
# .
# .
# 91%   to   100%

def main():
	numbers = []
	marksRangeFreq = []
	
	# initializing every list element with 0
	for i in range(10):
		marksRangeFreq.append(0)

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

	for i in range(0, len(numbers)):
		# if numbers[i] in range(0, 11):
		# 	marksRangeFreq[0] += 1
		# elif numbers[i] in range(11, 21):
		# 	marksRangeFreq[1] += 1
		# elif numbers[i] in range(21, 31):
		# 	marksRangeFreq[2] += 1
		# elif numbers[i] in range(31, 41):
		# 	marksRangeFreq[3] += 1
		# elif numbers[i] in range(41, 51):
		# 	marksRangeFreq[4] += 1
		# elif numbers[i] in range(51, 61):
		# 	marksRangeFreq[5] += 1
		# elif numbers[i] in range(61, 71):
		# 	marksRangeFreq[6] += 1
		# elif numbers[i] in range(71, 81):
		# 	marksRangeFreq[7] += 1
		# elif numbers[i] in range(81, 91):
		# 	marksRangeFreq[8] += 1
		# elif numbers[i] in range(91, 101):
		# 	marksRangeFreq[9] += 1
		if numbers[i] == 0:
			marksRangeFreq[0] += 1
			continue
		start = 1
		end = 11
		for j in range(10):
			if numbers[i] in range(start, end):
				marksRangeFreq[j] += 1
			start += 10
			end += 10
				
	print("Mark-Range \t\t Frequency")
	print("----------------------------------")
	start = 11
	end = 20
	print(f"0-10% \t\t\t {marksRangeFreq[0]}")
	for i in range(1, 10):
		print(f"{start}%-{end}% \t\t {marksRangeFreq[i]}")
		start += 10
		end += 10

if __name__ == '__main__':
	main()
