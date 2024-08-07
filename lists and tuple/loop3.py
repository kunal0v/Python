x=int(input("Enter the no.:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(0,x+1):
    for j in range(x-1,i,-1):
        print("*",end="")
    print()