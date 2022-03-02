st = input("Enter a string: ")

re = ""

if st[0] and st[-1] == "x":
    re = st.replace("x", "")
    print(re)
else:
    print(st)