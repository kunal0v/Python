x=int(input("Enter the no.: "));
for i in range(1,x+1):
    count=0;
    for j in range(1,i+1):
        if(i%j==0):
            count+=1;
    if(count==2):
        print(i)

