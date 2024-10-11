a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>b and a>c):
    print("the greatest no. ",a)
elif(b>c and b>a):
    print("the greatest no. ",b)
elif(c>a and c>b):
    print("the greatest no. ",c)
else:
    print("Enter correct value or different value.")