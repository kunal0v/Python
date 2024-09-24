# Tuple: immutable and cant changes the value and can't add and remove the elements
tup=(1,2,2,5.6,3)
listt=[]
for i in tup:
    listt.append(i)
print(listt)


# SECOND METHOD =>

print(list(tup))

