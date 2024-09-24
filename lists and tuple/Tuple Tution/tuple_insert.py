print("Enter 5 elements for tuple: ")

li = []
for i in range(5):
    y=int(input("Enter the value:"))
    li.append(y)

print(list(li))
print(tuple(li))