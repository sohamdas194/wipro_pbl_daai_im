# n = int(input("Enter a number: "))
# p = str(n)
# p = p[::-1]
# if str(n)==p:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")

n = int(input("Enter a number: "))
o = n
rev = 0
while (n > 0):
    rem = n % 10
    rev = (rev*10) + rem
    n = n//10
if o == rev:
    print("It's a palindrome")
else:
    print("It's not a palindrome")