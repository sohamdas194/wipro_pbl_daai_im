import math_module

while True:
    print("BASIC CALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())
        print("The result is", math_module.add(num1, num2))
        print()
        
    elif choice == 2:
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())
        print("The result is:", math_module.sub(num1, num2))
        print()
        
    elif choice == 3:
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())
        print("The result is:", math_module.mul(num1, num2))
        print()
        
    elif choice == 4:
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())
        print("The result is:", math_module.div(num1, num2))
        print()
    elif choice == 5:
        break
    else:
        print("You have entered a wrong choice, please enter your choice again")