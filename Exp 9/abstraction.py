from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

d = Dog()
d.sound()

c = Cat()
c.sound()





from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        radius = 5
        print("Area of Circle:", 3.14 * radius * radius)

class Rectangle(Shape):

    def area(self):
        length = 10
        breadth = 5
        print("Area of Rectangle:", length * breadth)

c = Circle()
c.area()

r = Rectangle()
r.area()





from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

class SBI(Bank):

    def withdraw(self, amount):
        balance = 10000

        if amount <= balance:
            print("Withdrawn:", amount)
            print("Remaining balance:", balance - amount)
        else:
            print("Insufficient balance")

account = SBI()
account.withdraw(3000)


