dic={
    "a":4,
    "b":5,
    "c":6,
}
x=list(dic.keys())[0]
y=list(dic.values())[0]
for i,j in dic.items():
    if(y<j):
        y=j
        x=i
print(x)