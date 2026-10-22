
# multi mdhe public,private,protected function access use krych
# destructor
# 5 types of inheritance


# student class 
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Constructor called")

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def __del__(self):
#         print("Destructor called")


# s1 = Student("Tanuja", 20)
# s1.display()

# del s1



# Student class with default constructor and destructor
# class Student:
#     def __init__(self):
#         self.name = "Tanuja"
#         self.age = 20
#         print("Constructor called")

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def __del__(self):
#         print("Destructor called")


# s1 = Student()
# s1.display()

# del s1



# Rectangle area
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         print("Constructor called")

#     def area(self):
#         print("Area =", self.length * self.breadth)

#     def __del__(self):
#         print("Destructor called")


# r = Rectangle(10, 5)
# r.area()

# del r



# Student class user input
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def __del__(self):
        print("Destructor called")


name = input("Enter name: ")
marks = int(input("Enter marks: "))

s = Student(name, marks)
s.display()

del s
