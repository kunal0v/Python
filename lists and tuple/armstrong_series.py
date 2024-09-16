for i in range (1,501):
    tem=i
    arm=0
    while(tem!=0):
        r=tem%10
        arm=arm+(r*r*r)
        tem=tem//10
    if(arm==i):
        print(i,"no is armstrong")