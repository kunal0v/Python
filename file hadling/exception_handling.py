# try : the portion where the error find 
# except : to show what's the error
try:
    x=int(input("Enter the first no. :"))
    y=int(input("Enter the Second no. :"))
    print(x/y)
except Exception as e:
    print(e)
print ("Rest of the code->")
