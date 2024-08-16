x=[4,5,6,7,3,2,66,99]
print(x)
y=int(input("Enter the no. of times the value comes:"))
count=0
for i in x:
    if(i==y):
        count+=1
print(count)