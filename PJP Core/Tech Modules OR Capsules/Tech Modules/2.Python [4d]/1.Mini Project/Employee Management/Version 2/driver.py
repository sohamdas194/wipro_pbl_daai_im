import math
from os.path import exists

# Importing the Employee class
from Employee import Employee

# Function to fetch employee details from emp.txt and store it in employee list
def fetch_emp_details():
	global employees

	# Checking if emp.txt exist or not, if not then the function ends
	try:
		emp_File = open('emp.txt', 'r')
	except FileNotFoundError:
		print("The file emp.txt doesn't exist")
		return

	# Fetching and isolating individual data from emp.txt
	# and inserting it as a Employee object in the employees list
	rows = emp_File.readlines()
	for i in range(3, len(rows)):
		row = rows[i]
		fields = row.split()
		new_emp = Employee(Empid = int(fields[0]), Ename = fields[1], Sal = float(fields[2]), Deptno = int(fields[3]))
		employees.append(new_emp)

# Function to validate employee ID
def validate_empid(empid):
	global employees

	# Checking if empid has 3 or more digits
	len_empid = math.floor(math.log10(empid)) + 1
	if len_empid < 3:
		print("Entered employee ID is less than 3 digits!! Try again")
		return False

	# Checking if empid already exist in storage
	for emp in employees: 
		if emp.Empid == empid:
			print("Entered employee ID already exists!! Try again")
			return False

	return True

# Function to validate salary
def validate_sal(sal):

	# Checking if sal is equal to or more than 3000	
	if sal < 3000:
		print("Salary should be more than 3000!! Try again")
		return False
	return True 

# Function to validate department number
def validate_deptno(deptno):

	# Checking if deptno is equal to 10 or 20 or 30
	if deptno in (10, 20, 30):
		return True
	print("Only accepted department numbers are 10, 20 and 30!! Try again")
	return False

# Function of add employee details to employee list and emp.txt
def Add_emp():
	# Taking input of employee ID and validating it
	try:
		empid = int(input("Enter employee ID: "))
	except:
		print("Invalid input!! Try again")
		return
	if validate_empid(empid) == False:
		return

	# Taking input of employee name and validating it
	try:
		ename = input("Enter employee's name: ").upper()
	except:
		print("Invalid input!! Try again")
		return

	# Taking input of employee salary and validating it
	try:
		sal = float(input("Enter employee's salary: "))
	except:
		print("Invalid input!! Try again")
		return
	if validate_sal(sal) == False:
		return

	# Taking input of employee department no. and validating it	
	try:
		deptno = int(input("Enter employee's department number: "))
	except:
		print("Invalid input!! Try again")
		return
	if validate_deptno(deptno) == False:
		return

	# Adding new employee details to employees list
	new_emp = Employee(Empid = empid, Ename = ename, Sal = sal, Deptno = deptno)
	employees.append(new_emp)

	# Creating and formatting the file emp.txt if it doesn't exist
	if exists('emp.txt') == False:
		temp_emp_File = open('emp.txt', 'w')
		temp_emp_File.write("~~~~~~~~~~~~~~~~~~Employees~~~~~~~~~~~~~~~~~~\n")
		temp_emp_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
		temp_emp_File.write('---------------------------------------------\n')
		temp_emp_File.close()
	
	# Adding new employee details to emp.txt 
	emp_File = open('emp.txt', 'a')
	emp_File.write(str(empid) + '\t\t' + ename + '\t\t' + str(sal) + '\t\t' + str(deptno) + '\n')
	emp_File.close()

	print("Employee successfully added")

# Function to display details of all employees
def Display_emp():
	global employees

	print("~~~~~~~~~~~~~~~~~~~~~~Employees~~~~~~~~~~~~~~~~~~~~~~~")
	print('EMPID\t\tENAME\t\tSAL\t\tDEPTNO')
	print('------------------------------------------------------')

	# Printing formatted employee details from employee list
	for emp in employees:
		print(str(emp.Empid) + '\t\t' + emp.Ename + '\t\t' + str(emp.Sal) + '\t\t' + str(emp.Deptno))

# Function to seperate employee data in 3 files depending on their department number
# emp_10.txt will have details of employees working in department 10
# emp_20.txt will have details of employees working in department 20
# emp_30.txt will have details of employees working in department 30
def Seperate_data():
	global employees

	# Creating and formatting emp_10.txt
	emp_10_File = open('emp_10.txt', 'w')
	emp_10_File.write("~~~~~~~Employees of department no. 10~~~~~~~\n")
	emp_10_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_10_File.write('---------------------------------------------\n')

	# Creating and formatting emp_20.txt
	emp_20_File = open('emp_20.txt', 'w')
	emp_20_File.write("~~~~~~~Employees of department no. 20~~~~~~~\n")
	emp_20_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_20_File.write('---------------------------------------------\n')

	# Creating and formatting emp_30.txt
	emp_30_File = open('emp_30.txt', 'w')
	emp_30_File.write("~~~~~~~Employees of department no. 30~~~~~~~\n")
	emp_30_File.write('EMPID\t\tENAME\t\tSAL\t\tDEPTNO\n')
	emp_30_File.write('---------------------------------------------\n')

	for emp in employees:
		# Fetching employee data and creating the formatted string to be inserted in the files
		row = str(emp.Empid) + '\t\t' + emp.Ename + '\t\t' + str(emp.Sal) + '\t\t' + str(emp.Deptno) + '\n'

		# Checking and inserting the employee details depending on their department no.
		if emp.Deptno == 10:
			emp_10_File.write(row)
		elif emp.Deptno == 20:
			emp_20_File.write(row)
		elif emp.Deptno == 30:
			emp_30_File.write(row)

	# Closing all file objects
	emp_10_File.close()
	emp_20_File.close()
	emp_30_File.close()

	print("All employee data has been seperated")

# Function to print and handle menu of the program
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

# main function
def main():
	# This list will store employee details for later use
	global employees
	employees = []

	# To Fetch employee details and store it into employees list
	fetch_emp_details()

	# To print the menu of the program
	menu()

if __name__ == '__main__':
	main()
