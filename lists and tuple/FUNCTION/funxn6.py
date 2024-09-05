# write a function "max of three (a,b,c)" that returns the maximum of three numbers 
def max_of_three(a,b,c):
    print("the greatest no.: ")
    if(a>b and a>c):
        print(a)
    if(b>c and b>a):
        print(b)
    if(c>a and c>b):
        print(c)
x=int(input("Enter the first no.:"))
y=int(input("Enter the second no.:"))
z=int(input("Enter the third no.:"))
max_of_three(x,y,z)
