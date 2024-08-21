x="Hello i  am world!"
count=1
for i in range(len(x)):
    if(x[i]==" "):
        if(x[i]==" " and x[i-1]==" "):
            continue
        else:
            count+=1
print(count)
