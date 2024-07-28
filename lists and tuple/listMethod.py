list=[2,1,5]
list.append(4) #ADDS ONE ELEMENT AT THE END and ALSO KNOWN AS MUTATING THE LIST
print(list)

list.sort() # ARRANGING ELEMENTS IN ASCENDING ORDER
print(list)
list.sort(reverse=True) # ARRANGING ELEMENTS IN DESCENDING ORDER
print(list)

list.reverse() #name.reverse() used to reverse the list
print(list)

#       name.insert(index,value)
list.insert(2,10)
print(list)

#       name.remove(VALUE)===> REMOVE FIRST OCCURENCE OF ELEMENT
list.remove(10)
print(list)

#   name.pop(INDEX)===> USED TO REMOVE OR POP THE INDEX FORM LIST
list.pop(1)
print(list)
