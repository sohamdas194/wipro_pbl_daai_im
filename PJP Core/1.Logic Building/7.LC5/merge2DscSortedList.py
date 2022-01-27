# Design an algorithm to accept element for 2 random arrays. Rearrange the array elements in descending order then merge them into form one array.

def merge2DscSortedLists(list1, list2):
	list3 = []

	m = len(list1)
	n = len(list2)

	i = j = 0

	while (i!=m and j!=n):
		if list1[i] > list2[j]:
			list3.append(list1[i])
			i += 1
		elif list2[j] > list1[i]:
			list3.append(list2[j])
			j += 1
		elif list1[i] == list2[j]:
			list3.append(list1[i])
			list3.append(list2[j])
			i += 1
			j += 1

	while (i < m):
		list3.append(list1[i])
		i += 1

	while (j < n):
		list3.append(list2[j])
		j += 1

	return list3

from sortListDsc import sortDsc

def main():
	list1 = []
	list2 = []

	m = int(input("Enter size of the first list:"))
	print("Enter elements in the first list one by one")
	for i in range(m):
		list1.append(int(input()))

	n = int(input("Enter size of the second list:"))
	print("Enter elements in the second list one by one")
	for i in range(n):
		list2.append(int(input()))

	# sorting the lists
	list1 = sortDsc(list1)
	list2 = sortDsc(list2)

	list3 = merge2DscSortedLists(list1, list2)

	print(list3)

if __name__ == '__main__':
	main()
