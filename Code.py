class Animal:
    def __init__(self,name:str):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

pet1 = Dog("Carlos")
print(pet1.bark())

class Room:
    def __init__ (self,name: str):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom") ]

House1 = House()
for room in House1.rooms:
    print (f"Room Created: {room.name}")