a=[0,1,2,3,6,9,10,15,16]
y=[]
z=len(a)
for i in range(0,len(a)+1,2):
    if(i<len(a)-1):
        y.append(a[i]+a[i+1])
if(len(a)%2!=0):
    y.append(a[z-1])
print(y)