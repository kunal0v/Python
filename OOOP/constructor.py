class Animal:
    def __init__(self,a,b,c,d):
        self.legs= a
        self.eyes= b
        self.types= c
        self.name= d
a1=Animal(4,2,"Herbivorous","donkey")
a2=Animal(2,2,"Carnivorous","Cheetah")
a3=Animal(4,2,"Omnivorous","Lion")
a4=Animal(4,2,"Omnivorous","Tiger")
print(a1.name,a4.types)