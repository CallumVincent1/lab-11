class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} is {self.age} years old")
        
class Job:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def __str__(self) -> str:
        return (f"job name is {self.job_title} and has a salary of {self.salary}")

class Employee(Person,Job):
    def __init__(self, name, age, job_title, salary):
        Person.__init__(self, name, age)
        Job.__init__(self, job_title, salary)

    def __str__(self):
        return (f"{self.name} is {self.age} and has the job {self.job_title} and makes {self.salary}")
    

employee1 = Employee("john", 23, "developer", 43000)
print(employee1)