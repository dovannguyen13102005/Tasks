from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def get_in4(self):       #Abstraction
        pass
    @abstractmethod
    def talk(self):          #Abstraction
        pass



#Encapsulation
class Dog(Animal):
    def __init__(self, name):
        self.__name = name
    def get_in4(self):
        return f"Name of dog is: {self.__name}"
    def talk(self):
        return f"{self.__name} keu gau gau"

#Encapsulation
class Cat(Animal):
    def __init__(self, name):
        self.__name = name
    def get_in4(self):
        return f"Name of cat is: {self.__name}"
    def talk(self):
        return f"{self.__name} keu meo meo"
#Inheritance
class Tabby(Cat):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age
    def get_in4(self):
        return (f"{super().get_in4()}\n"
                f"Age: {self.__age}")

animals = [Dog("Trung"), Cat("Nam"), Tabby("Hoang", 8)]
#Polymorphism
for animal in animals:
    print("\n" + animal.get_in4())
    print(animal.talk())
