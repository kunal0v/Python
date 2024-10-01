a=19
print(id(a))
a=38
print(id(a))
# hence variable are immutable
dic={
    "name":"Ramu",
    "class":12,
    "school":34,
}
li=list(dic.items())
print(li)
li.sort()
y=dict(li)
print(y)
