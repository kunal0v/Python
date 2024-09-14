x=[2,3,4,5,6,7,7,8,3,4,4,4,4,5,5,5]
y=[]
a=int(input("Enter  the  no.: "))
for i in x:
    count=0 
    for j in x:
        if(i==j):
            count=count+1
    if(count==a):
        if(i in y):
            continue
        else:
            y.append(i)
print(y)
    

        
