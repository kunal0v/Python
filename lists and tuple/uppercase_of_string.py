x = input("Enter the sentence:")
y=""
y+=x[0].upper()
for i in range(1,len(x)):
    if(x[i-1]==" "):
        y+=x[i].upper()
    else:
        y+=x[i].lower()
print(y)