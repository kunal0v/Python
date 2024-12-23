# x=lambda a,b,c:a**b**c 
# print(x(5,2,2))

z=int(input("Enter the value:"))
x=lambda a:a%2==0

b=(x(z))
if(b==False):
    print("yes it is an odd no.")
else:
    print("even no.")