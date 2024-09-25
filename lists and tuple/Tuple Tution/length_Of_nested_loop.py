tuppp=(1,2,44,56,(4,5,6,76),3,4,5,(4,5,6,76,7,3))
count=len(tuppp)
for i in tuppp:
    if (type(i)==tuple):
        count=count +len(i)
        count=count-1
print(count)