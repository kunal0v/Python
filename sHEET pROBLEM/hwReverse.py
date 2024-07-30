x=input("Enter the String:")
y = ""
length=len(x)
for i in range(length-1,-1,-1):
    y+=x[i]
print("the reverse of a string is:",y)
if(x==y):
    print("Yes it is a palindrome")
else:
    print("No it is a palindrome")