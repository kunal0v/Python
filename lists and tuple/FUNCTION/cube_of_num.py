x=int(input("Enter the first value:"))
y=int(input("Enter the second value:"))
def cub(x,y):
    if y==0:
        return 1
    else:
        return x*cub(x,y-1)
print(cub(x,y))