x=int(input("Enter the no. :"))
z=x
arm=0
count=len(str(x))
print("count :",count)
while(x!=0):
    r=x%10
    arm=arm+r**count
    x=x//10
print("arm =",arm)
if(arm==z):
    print("Yes it is a armstrong")
else:
    print("No it is not a armstrong")