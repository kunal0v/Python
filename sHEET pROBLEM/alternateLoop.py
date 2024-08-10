x=int(input("Enter the no.:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        if(j%2==0):
            print("0",end=" ")
        print()
        if(j%2==1):
            print("1",end="")