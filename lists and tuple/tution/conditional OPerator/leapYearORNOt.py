x=int(input("Enter the year:"))
if(x%4==0 and x%100==0):
    print("Yes It's a leap year");
elif(x%100==0):
    print("yes it is a leap year...");
else:
    print("No It's a leap year");