x=int (input("Enter the value :"))
y=x
pd=0
while(x!=0):
    r= x%10
    print(r)
    pd=pd*10+r
    print(pd)
    x=x//10
    print(x)
# if(y==pd):
#     print("Pallindrome detected")
# else:
#     print("Pallindrome Not detected")
