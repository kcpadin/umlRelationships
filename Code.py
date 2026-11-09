# INHERITAMNCE
class Animal:
    def __init__(self,name:str):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} barks. They cant meow. they are't a cat."

pet1 = Dog("Carlos")
print(pet1.bark())

#CPOMPOSITION

class Room:
    def __init__ (self,name: str):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom") ]

House1 = House()
for room in House1.rooms:
    print (f"Room Created: {room.name}")

my_house = House()
for room in my_house.rooms:
    print (r"Room created: {room.name}")

#Aggregatorion 

class Book:
    def __init__(self,title: str):
        self.title = title

    def __del__(sefl):
        print(f"Book has been claimed by the Guest. '{self.title}' is no longer in your hands.")

class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books else []

    def __del__(self):
        print ("The Library has been destroyed by the Arbiters.")
book1 = Book("Book of Salvador")
book2 = Book("Book of Yuna")

my_library = Library([book1, book2])
print (f"Library has: {b.title for b in my_library.books]}")

print ("\nArbiters arriving at The Library...")
del my_library

print ("\nChecking books after destruction of The Library")
print (f"Still active in The City -> book1: {book1.title}")

print (f"Still active in The City -> book2: {book2.title}")

#Association
