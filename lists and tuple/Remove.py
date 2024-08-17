# program that removes an element specified by the user
x=[1,2,3,4,5,6,7,8,9]
y=int(input("Enter the value that you want to remove:"))
if(y not in x):
    print("no. not found:")
else:
    for i in x:
        if(i==y):
            x.pop(i-1)
    print(x)
