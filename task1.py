class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

class Dog(Animal):
    def __init__(self, name, age, sound, breed):
        super().__init__(name, age, sound)
        self.breed = breed
    
    def display_info(self):
        print(f"Dog name: {self.name}")
        print(f"age: {self.age}")
        print(f"breed: {self.breed}")
        print(f"sound: {self.sound}")

dog_instance = Dog("buddy", 3, "bark", "labrador")
dog_instance.display_info()
print(f"data type of dog instance: {type(dog_instance)}")