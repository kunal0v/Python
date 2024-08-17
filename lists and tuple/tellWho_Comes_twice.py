x=[8,8,2,3,4,5,6,6,7]

for i in x:
    count=0
    for j in x:
        if(i==j):
            count+=1
    if(count>1):
        print("sorry list is not unique...")
        break
if(count==1):
    print("list is unique...")        