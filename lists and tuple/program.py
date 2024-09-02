x = input("Enter the value: ")

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'\""
numbers = "1234567890"
decimal = "."

alp = False
num = False
dec = False

for i in alphabets:
    if i in x:
        alp = True
        
for j in numbers:
    if j in x:
        num = True
        
for k in decimal:
    if k in x:
        dec = True
        
y = x.count(".")
if dec==True and num==True and y==1 and alp==False:
    print("Float")
    
    
elif num==True and dec==False and alp==False:
    print("Integers")

else:
    print("string")