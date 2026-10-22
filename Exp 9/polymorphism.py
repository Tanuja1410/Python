
# class Animal:
#     def sound(self):
#         print("Animals make sounds")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")


# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()





### 2. Vehicle – Polymorphism


class Car:
    def move(self):
        print("Car moves on the road")


class Boat:
    def move(self):
        print("Boat moves on water")


class Plane:
    def move(self):
        print("Plane flies in the air")


for vehicle in [Car(), Boat(), Plane()]:
    vehicle.move()







class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("Addition:", num1 + num2)
