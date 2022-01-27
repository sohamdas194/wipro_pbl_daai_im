# Design an algorithm to accept 10 integer elements for an array and rearrange the elements in descending order. The new array must be printed to the user.

def sortDsc(lst):
	i = 0
	n = len(lst)
	while i < n-1:
		j = 0
		while j < n-i-1:
			if lst[j] < lst[j+1]:
				temp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = temp
			j += 1
		i += 1
	return lst

def main():
	lst = []

	n = int(input("Enter size of the list:"))
	print("Enter elements in the first list one by one")
	for i in range(n):
		lst.append(int(input()))

	sortDsc(lst)

	print("After sorting: ", lst)

if __name__ == '__main__':
	main()
