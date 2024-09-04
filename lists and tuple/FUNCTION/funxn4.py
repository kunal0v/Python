# write a function factorial(n) that returns the factorial of a given no. using a loop 
def factorial(x):
    y=1
    for i in range(1,x+1):
        y=y*i
    print(y)
x=int(input("Enter the no.:"))
factorial(x)
