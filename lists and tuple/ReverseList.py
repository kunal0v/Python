x=[8,5,9,6]
y= (x[::-1])
sum=[]
for i in range(len(x)):
    sum[i]=x[i]+y[i]
    sum.append(sum[i])
print(sum[i])





















