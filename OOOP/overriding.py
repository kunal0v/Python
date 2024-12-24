class Animal:
    legs=4
    eyes=2
    types="Herbivorous"
    def add(self,a):
        print("BARK")
    def add(self,a,b):
        print("Don't Bark")
    def run(self):
        print("run")
a1=Animal()
a1.add(5,4)