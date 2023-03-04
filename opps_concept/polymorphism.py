class Animal:
    def woq(self):
        print("This is parent class")

class Child(Animal):
    def woq(self):
        print("This is child class")

animal = Animal()
animal.woq()

child = Child()
child.woq()