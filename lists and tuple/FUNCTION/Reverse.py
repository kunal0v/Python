x=input('Enter the string:')
def rev(x):
    if (len(x) == 0):
        return ""
    if(len(x)!=0):
        return x[-1] + rev(x[:-1:])
print(rev(x))