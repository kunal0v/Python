x=int(input("Enter the no.: "));
count=0
bill=0
for i in range(1,x+1):
    if(x%i==0):
        count+=1;
if(count==2):
    print("Yes it is a prime nO.");
else:
    print("No it is not a prime nO.");