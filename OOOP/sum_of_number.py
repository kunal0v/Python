x=int(input("enter the three digit number:"))
y=x%10
print(y)
a=x%100
print(a)
b=a//10
print(b)
z=x//100
print(z)
print("sum=",z+b+y)