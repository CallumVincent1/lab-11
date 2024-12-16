class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f"This is an instance of person class whose name is {self.name}, and age is {self.age} years")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"This is an instance of Dog class whose name is {self.name}, and age is {self.age} years")