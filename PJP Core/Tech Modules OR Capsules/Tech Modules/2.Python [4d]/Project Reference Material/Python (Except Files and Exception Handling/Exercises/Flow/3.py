n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

n1 = n1 % 10
n2 = n2 % 10
if n1 == n2:
    print("Last digits are equal")
else:
    print("Last digits are not equal")