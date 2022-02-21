# Given a set of 3 student's examination marks (in the range from 0 to 100), make a count of the number of students that have passed the exam. A pass is awarded if the students mark is greater than or equal to 35.

class Student:
	def __init__(self, marks):
		self.marks = marks

if __name__ == '__main__':
	s1 = Student([35, 45, 65, 20, 56])
	s2 = Student([35, 45, 65, 60, 53])
	s3 = Student([35, 45, 65, 40, 36])

	count = 0 

	count+=1
	for mark in s1.marks:
		if mark < 35:
			count-=1
			break

	count+=1
	for mark in s2.marks:
		if mark < 35:
			count-=1
			break

	count+=1
	for mark in s3.marks:
		if mark < 35:
			count-=1
			break

	print('Number of Student that passed the exam:', count)