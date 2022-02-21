# Given a set of 3 student's examination marks (in the range from 0 to 100), make a count of the number of students that have passed the exam. A pass is awarded if the students mark is greater than or equal to 35.

if __name__ == '__main__':

	n = 3
	# n = int(input("Enter the number of students: "))
	marks = []
	print("Enter the marks of the students one by one: ")
	for i in range(n):
		marks.append(int(input()))

	count = 0
	for mark in marks:
		if mark >= 35:
			count+=1

	print("No. of students that passed the exams:", count)
