import sys

n = len(sys.argv)
s = 0
li = []

for i in range(1, n):
    li.append(int(sys.argv[i]))
    
for i in li:
    for j in range(2, i):
        if(i % j == 0):
            break;
    else:
        s += i
        
print(s)