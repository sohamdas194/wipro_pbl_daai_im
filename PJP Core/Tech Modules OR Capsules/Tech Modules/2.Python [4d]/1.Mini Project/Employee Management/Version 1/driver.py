import math
from os.path import exists


def validate_empid(empid):

	len_empid = math.floor(math.log10(empid)) + 1
	if len_empid < 3:
		return False
	
	try:
		emp_File = open('emp.txt', 'r')
	except FileNotFoundError:
		return True

	lines = emp_File.readlines()
	for i in range(3, len(lines)):
		line = lines[i]
		existing_emp_id = int(line[:line.find('\t')])

		if existing_emp_id == empid:
			emp_File.close()
			return False

	emp_File.close()
	return True


def validate_sal(sal):
	if sal < 3000:
		return False
	return True 


def validate_deptno(deptno):
	if deptno in (10, 20, 30):
		return True
	return False


def Add_emp():
	try:
		empid = int(input("Enter employee ID: "))
	except:
		print("Invalid input!! Try again")
		return

	if validate_empid(empid) == False:
		print("Entered Empid already exists or is less than 3 digits!! Try again")
		return

	try:
		ename = input("Enter employee's name: ").upper()
	except:
		print("Invalid input!! Try again")
		return

	try:
		sal = float(input("Enter employee's salary: "))
	except:
		print("Invalid input!! Try again")
		return

	if validate_sal(sal) == False:
		print("Salary should be more than 3000!! Try again")
		return

	try:
		deptno = int(input("Enter employee's department number: "))
	except:
		print("Invalid input!! Try again")
		return

	if validate_deptno(deptno) == False:
		print("Only accepted department numbers are 10, 20 and 30!! Try again")
		return

	if exists('emp.txt') == False:
		temp_emp_File = open('emp.txt', 'w')
		temp_emp_File.write("~~~~~~~~~~~~~~~~~~Employees~~~~~~~~~~~~~~~~~~\n")
		temp_emp_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
		temp_emp_File.write('---------------------------------------------\n')
		temp_emp_File.close()
		
	emp_File = open('emp.txt', 'a')
	emp_File.write(str(empid) + '\t\t' + ename + '\t\t' + str(sal) + '\t\t' + str(deptno) + '\n')
	emp_File.close()

	print("Employee successfully added")


def Display_emp():
	try:
		emp_File = open('emp.txt', 'r')
	except FileNotFoundError:
		print("The file emp.txt doesn't exist")
		return

	print("~~~~~~~~~~~~~~~~~~~~~~Employees~~~~~~~~~~~~~~~~~~~~~~~")
	print('EMPID\t\tENAME\t\tSAL\t\tDEPTNO')
	print('------------------------------------------------------')

	lines = emp_File.readlines()
	for i in range(3, len(lines)):
		print(lines[i], end='')

	emp_File.close()


def Seperate_data():
	try:
		emp_File = open('emp.txt', 'r')
	except FileNotFoundError:
		print("Error!! emp.txt file doesn't exist")
		return

	emp_10_File = open('emp_10.txt', 'w')
	emp_10_File.write("~~~~~~~Employees of department no. 10~~~~~~~\n")
	emp_10_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_10_File.write('---------------------------------------------\n')

	emp_20_File = open('emp_20.txt', 'w')
	emp_20_File.write("~~~~~~~Employees of department no. 20~~~~~~~\n")
	emp_20_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_20_File.write('---------------------------------------------\n')

	emp_30_File = open('emp_30.txt', 'w')
	emp_30_File.write("~~~~~~~Employees of department no. 30~~~~~~~\n")
	emp_30_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_30_File.write('---------------------------------------------\n')

	lines = emp_File.readlines()
	for i in range(3, len(lines)):
		line = lines[i]
		deptno = int((line[line.rfind('\t')+1:-1]))

		if deptno == 10:
			emp_10_File.write(line)
		elif deptno == 20:
			emp_20_File.write(line)
		elif deptno == 30:
			emp_30_File.write(line)

	emp_File.close()
	emp_10_File.close()
	emp_20_File.close()
	emp_30_File.close()

	print("All employee data has been seperated")


def menu():
	print("\nEmployee Managment System")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Enter ->")
	print("1. Add_emp")
	print("2. Display_emp")
	print("3. Separate_emp")
	print("4. Exit")

	choice = input("Enter your choice: ")
	print()

	if choice == '1':
		Add_emp()
		menu()

	elif choice == '2':
		Display_emp()
		menu()

	elif choice == '3':
		Seperate_data()
		menu()

	elif choice == '4':	
		exit(0)

	else:
		print("Invalid choice!! Try again")
		menu()


def main():
	menu()

if __name__ == '__main__':
	main()
