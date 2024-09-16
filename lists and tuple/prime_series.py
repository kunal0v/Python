x=int(input("Enter the first no.:"))
y=int(input("Enter the second no.:"))
for i in range(x,y+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(" prime No. are:",i)
