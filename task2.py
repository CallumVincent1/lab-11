class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return (f"{self.name} has a salary of {self.salary}")
    
class Manager(Employee):
    def __init__(self,name,salary,department_name):
        super().__init__(name,salary)
        self.depertment = department_name

    def __str__(self):
        return (f"{self.name} has a salary of {self.salary} and is the {self.depertment} head")
    
class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def __str__(self):
        return (f"{self.name} has a salary of {self.salary} and uses the {self.programming_language} programming language")   

dev1 = Developer("john", 43000, "python")
print(dev1)