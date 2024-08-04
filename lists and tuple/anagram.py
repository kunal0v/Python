x=input("enter the value:")
y=input("Enter any sentence")
y=y.lower()
x=x.lower()
count=0
count=len(x)
# z=count
for i in x:
    if(i in y):
        count+=1

for j in y:
    if(j in y):
        count+=1

if(i==j):
    print("it is anagrams")
else:
    print("it is not a anagrams")