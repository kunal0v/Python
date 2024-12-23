# x=int(input("Enter the value for factorial:"))
# count=1
# for i in range(1,x+1):
#     count =count*i
# print(count)

# program for prime number series
# x=int(input("Enter the first value:"))
# y=int(input("enter the last value:"))
# for i in range(x,y+1):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print("Prime no.: ",i)

# program for prime number 
x=int(input("Enter the  value:"))
count=0
for  i in range(1,x+1):
    if(x%i==0):
        count=count+1
if(count==2):
    print("prime number")
else:
    print("not a prime number")