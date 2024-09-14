x=int(input("Enter the value:"))
a=0
b=1
print(a)
print(b)
for i in range(0,x-2):
    z=a+b
    a=b
    b=z
    print(z)
