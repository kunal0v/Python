x=int(input("Enter the value:"))
for i in range (1,x):
    for j in range(1,x-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if(i==1 or i==x or k==1 or k==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
