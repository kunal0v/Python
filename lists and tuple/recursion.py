def recursion(n):
    if(n==1):
        return 1
    else:
        print(n)
        recursion(n-1)
recursion(5)