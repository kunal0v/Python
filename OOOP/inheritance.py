class Animal:
    def sound(self):
        print("Make sound")
    legs=4
    eyes=2
    color="black"
class Dog(Animal):
    types="omnivorous"
d1=Dog()
print(d1.legs,d1.sound())