x=input("Enter the sentence:")
wc=0
ch=False
y="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in x:
    if(i!=" "):
        if not ch:
            wc+=1
            ch=True
    else:
        ch=False
print(wc)
