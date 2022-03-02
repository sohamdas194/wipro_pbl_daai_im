dic1 = {1:10, 2:20}
dic2 = {3:30, 4:50}
dic3 = {5:50, 6:60}

# dic4 = dic1.copy()
# dic4.update(dic2)
# dic4.update(dic3)

#OR

dic4 = dic1 | dic2 | dic3

print(dic4)
