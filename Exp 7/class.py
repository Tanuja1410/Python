class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Tanuja", 20)
s1.display()



# default constructor
class Student:
    def __init__(self):
        self.name = "Tanuja"
        self.age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student()
s1.display()


# calculate area
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area =", self.length * self.breadth)


r = Rectangle(10, 5)
r.area()


# Class with Constructor and User Input
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter name: ")
marks = int(input("Enter marks: "))

s = Student(name, marks)
s.display()