#Swap the variables without using third variables:
a=int(input("Enter a:"));
b=int(input("Enter b:"));
a,b=b,a
print("a:",a)
print("b:",b)