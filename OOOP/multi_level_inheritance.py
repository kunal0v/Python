class Animal:
    def sound(self):
        print("Make sound")
    legs=4
    eyes=2
    color="black"
class Dog(Animal):
    types="omnivorous"
class lebra(Dog):
    nature="friendly"
d1=lebra()
print(d1.legs,d1.sound(),d1.types,d1.nature)