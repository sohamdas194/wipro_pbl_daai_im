# Design an algorithm to accept 25 integer elements for an array. Then find the number with the maximum value in the set and the position.
# - where it occurs first
# - where it occurs last

def findMaxValNdItsPos(lst):
	maxVal = lst[0]
	maxValStartPos = maxValLastPos = -1

	for i in range(len(lst)):
		if lst[i] >= maxVal:
			maxVal = lst[i]

			if maxValStartPos == -1 or lst[maxValStartPos] != lst[i]:
				maxValStartPos = i

			maxValLastPos = i

	if maxValStartPos == -1:
		maxValStartPos = maxValLastPos = 0
	
	print("Max value:", maxVal)
	print("It occurs first at:", maxValStartPos)
	print("It occurs last at:", maxValLastPos)


def main():
	lst = []

	# n = int(input("Enter size of the list:"))
	n = 25
	print("Enter 25 elements in the first list one by one")
	for i in range(n):
		lst.append(int(input()))

	findMaxValNdItsPos(lst)

if __name__ == '__main__':
	main()
