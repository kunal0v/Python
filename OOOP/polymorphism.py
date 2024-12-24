# POLYMORPHISM: The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes
class Animal():
    legs=4
    eyes=2
    types="omnivorous"
    def sound(self):
        print("Bark")
class Birds:
    fly=True
    bones="Hollow"
    def fly(self):
        print("Yes it can fly")
    def sound(self):
        print("Chirp")
b1=Birds()
b1.sound()
