x=[5,9,69,86,6,3,7]
o=[]
e=[]
for i in x:
    if(i%2==0):
        e=e+[i]
    else:
        o=o+[i]
print("even no. are :",e)
print("odd no. are :",o)