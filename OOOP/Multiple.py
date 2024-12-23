class Animal:
    def sound(self):
        print("Make sound")
    eyes=2
    color="black"
class Bird():
    types="omnivorous"
    fly="True"
class Bat(Animal):
    eat=True
    nature="friendly"
class Insect (Animal):
    eat=True
    nature="friendly"
d1=Insect()
d2=Bird()

print(d1.sound(),d2.types,d1.nature,d2.fly)