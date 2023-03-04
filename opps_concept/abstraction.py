from decimal import Clamped


class Car:
    def __init__(self,name):
        pass
        self.name = name
        # self.id = id 
        # self.income = income

    def add(self):
        pass
        # print(self.name)


class Tesla(Car):
    def color(self):
        print('The colore is Black')

class Audi(Car):
    def color(self):
        print('The colore is Red')

class Aulto(Car):
    def color(self):
        print('The colore is Yello')

class Test(Car):
    def add(self):
        print(self.name)


text = Test('kp')
text.add()

t = Tesla('let')
t.color()

# A = Audi()
# A.color()

# AU = Aulto()
# AU.color()