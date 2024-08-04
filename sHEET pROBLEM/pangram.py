x="abcdefghijklmnopqrstuvwxyz"
y=input("Enter any sentence")
y=y.lower()
count=0
for i in x:
    if(i in y):
        count+=1
if(count==26):
    print("it is pangrams")
else:
    print("it is not a pangrams")