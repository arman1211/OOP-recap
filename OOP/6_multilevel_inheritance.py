# eta bolte pari child class inherit hobe parent class theke, parent class inherit hobe grandparent class teke. GrandParent->Parent->Child

# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

# Parent class 
class Mammal(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)  
        self.habitat = habitat
    
    def description(self):
        return f"{self.name} lives in {self.habitat}."

# Child class 
class Dog(Mammal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)  
        self.breed = breed
    
    # Overriding the speak method
    def speak(self):
        return f"{self.name}, {self.breed}, barks."


dog = Dog("deshi", "house", "gew gew")

print(dog.speak()) 
print(dog.description())  
print(Dog.mro())
