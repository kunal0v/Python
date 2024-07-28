weight=float(input("Enter your weight:"));
height=float(input("Enter your height:"));
bmi=weight/(height*height)
if(bmi<18.5):
    print("Underweight")
elif(bmi>18.5 and bmi<24.9):
    print("healthy weight")
elif(bmi>25 and bmi<29.0):
    print("overweight")
elif(bmi>30):
    print("obesity")