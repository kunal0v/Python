x=int(input("Enter the value:"))
for i in range (1,x+1):
    for j in range(1,x-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print(end="")
    for j in range(1,2*j):
        print(" ",end="")
    for k in range(1,2*i):
        if (k==2*x-1):
            continue
        else:
            print("*",end="")
    print()
