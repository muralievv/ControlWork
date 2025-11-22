class Person:
    def set_age(self, age: int):
        self._age = age
    def get_age(self):
        if self._age >= 0:
         return self._age
        else:
            print(f"Ошибка, возраст не может быть меньше 0")

p = Person()
p.set_age(25)

print(p.get_age())

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"I am an animal"
class Dog(Animal):
    def speak(self):
        return f"Woof"
class Cat(Animal):
    def speak(self):
        return f"Meow"
dog = Dog("buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())
class Vehicle:
    def move(self):
        return f"Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return f"Car is driving"
class Bicycle(Vehicle):
    def move(self):
        return f"Bicycle is pedaling"
def move(vehicle):
    print (vehicle.move())
car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
     def __init__(self, width, height):
         self.width = width
         self.height = height
     def area(self):
         return self.height * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.14
rect = Rectangle(10,5)
circle = Circle(7)
print(rect.area())
print(circle.area())