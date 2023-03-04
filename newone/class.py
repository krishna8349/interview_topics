class Student:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def detail(self,name):
        print("My name is "+name)


class Derived(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

der  = Derived("Mukesh",29)

student = Student("Krishna", 21)
print(student.name)
print(der.name)