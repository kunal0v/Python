x=int(input("Enter the value"))
if((x%100!=0 and x%4==0)or x%400==0):
    print("yes it is a leap year")
else:
    print("no it is a leap year")