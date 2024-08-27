x = input("Enter the sentence: ")
count = 0
ch = False

for i in range(len(x)):
    if x[i] != " ":
        if not ch:
            count += 1
            ch = True
    else:
        ch = False
print(count)