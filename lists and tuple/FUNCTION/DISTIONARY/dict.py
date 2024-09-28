# DICTIONARY: IT IS THE COLLECTION OF KEY AND VALUES  WHICH MAKES ITEM
dic ={
    "Name": "Kunal",
    "Program": "BCA",
    "Year":19,
    "name": "Tina",
}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

# how to get particular values
print(dic["Name"])
print(dic.get("Name"))
dic["country"]="India"
#for updation 
dic["name"]="Kamal"
print(dic)           