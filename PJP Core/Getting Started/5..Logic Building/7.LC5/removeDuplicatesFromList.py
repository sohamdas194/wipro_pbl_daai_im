# Design an algorithm to remove all duplicate elements from an ordered array (may be ascending or descending order) and contract the array accordingly.

def removeDuplicatesFromList(lst):
	i = 0
	while i < len(lst)-1:
		while lst[i] == lst[i+1]:
			lst.pop(i+1)
		i += 1

def main():
	lst = []

	n = int(input("Enter size of the list:"))
	print("Enter elements in the first list one by one")
	for i in range(n):
		lst.append(int(input()))

	lst.sort()
	removeDuplicatesFromList(lst)

	print("After removing duplicates: ", lst)

if __name__ == '__main__':
	main()
