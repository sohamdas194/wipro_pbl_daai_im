st = input("Enter a string: ")

n = int(input("Enter the number of repetitions: "))

strev = st[-n::]

for i in range(0,n):
    print(strev, end="")