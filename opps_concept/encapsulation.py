class Person:
    def __init__(self,name ,income):
        self.name = name
        self.__income = income

    def add_income(self):
        self.name
        self.__income
    
person = Person('kp',30000)
print(person.__income)