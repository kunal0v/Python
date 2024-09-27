def pal(x):
    if(len(x) <=1):
        return True
    elif x[0]!=x[-1]:
        return False
    else:
        return pal(x[1:-1:])
print(pal("naman"))