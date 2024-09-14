# Wap a python program that will remove the duplicate elements form the list 
a=[3,4,5,6,3,7,5]
b=[]
for i in a:
    if(i in b):
        continue
    else:
        b.append(i)
print(b)