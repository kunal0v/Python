x=[1,2,3]
y=[]
for i in x:
    for j in x:
        for k in x:
            if(i != j and j != k and k != i):
                    print([i,j,k])