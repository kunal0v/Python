x=input("Enter the String:")
y = ""
for i in range(len(x)-1,-1,-1):
    y+=x[i]
print(y)