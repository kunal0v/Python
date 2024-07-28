x=int(input("Enter the number:"))
for i in range(0,x+1):
    if(i%3==0 and i%5!=0):
        print(i)