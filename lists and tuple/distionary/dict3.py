n1=["name","age","city"]
n2=["alice","25","New York"]
dit={}
for i in range(0,3):
    dit[i]={n1[i]:n2[i]}
dict(dit)
print(dit)