x=input('Enter the string:')
def rev(x):
    if (len(x) == 0):
        return ""
    if(len(x)!=0):
        return x[-1] + rev(x[:-1:])
def pal():
    if(rev(x) == x):
        print("pallindrome")
    else:
        print("not pallindrome")
print(rev(x))
pal()