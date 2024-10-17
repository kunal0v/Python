# raise: to customise the error.
try:
    x=int(input("enter the value:"))
    if(x<=0):
        raise ValueError
except ValueError:
    print("Please enter correct age")
else:
    print(x)

# try:
#     x=int(input("enter the value:"))
#     if(x<=0):
#         raise ValueError
# except Exception :
#     print("error")
# else:
#     print(x)