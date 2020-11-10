class Animal():

    def __init__(self):
        print("animal created")
    
    def whoAmI(self):
        print("animal")
    
    def eat(self):
        print("eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog crated")
    
    def bark(self):
        print("Woof")

    def eat(self):
        print("dog eating")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
