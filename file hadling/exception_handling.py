# try : the portion where the error find 
# except : to show what's the error
#else: When no error is found 
#finally: at the end of the try to complete whether there is an error or not
# try:
#     x=int(input("Enter the first no. :"))
#     y=int(input("Enter the Second no. :"))
#     print(x/y)
# except Exception as e:
#     print(e)
# print ("Rest of the code->")

try:
    x=int(input("Enter the first no. :"))
    y=int(input("Enter the Second no. :"))
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(x/y)
finally:
    print("oh no!")
print ("Rest of the code->")
