a1=int(input("Enter the marks in hindi:"))
a2=int(input("Enter the marks in English:"))
a3=int(input("Enter the marks in Maths:"))
a4=int(input("Enter the marks in science:"))
a5=int(input("Enter the marks in Social Science:"))

sum=(a1+a2+a3+a4+a5)/5

if(sum>=60):
    print("First division")
elif(sum<60 and sum>=45):
    print("Second division")
elif(sum<45 and sum>=33):
    print("Third division")
else:
    print(" Sorry, better luck next time")
