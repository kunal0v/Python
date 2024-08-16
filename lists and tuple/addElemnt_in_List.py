x=[5]
x.append(3)
print(x)
x+=[11]

x.extend([55,22,99,66])
print(x)

x.insert(3,77)
print(x)
y=(x[::-1])
print(y)