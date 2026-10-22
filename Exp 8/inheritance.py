# Inheritance in Python


# single inheritance
class Animal:
    def eat(self):
        print("Animal lives")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()




# Multiple Inheritance
class Father:
    def father_property(self):
        print("Father's skills")

class Mother:
    def mother_property(self):
        print("Mother's skills")

class Child(Father, Mother):
    def child_property(self):
        print("Child has both skills")

c = Child()
c.father_property()
c.mother_property()
c.child_property()





# Multilevel Inheritance
class Grandfather:
    def show_grandfather(self):
        print("Grandfather")

class Father(Grandfather):
    def show_father(self):
        print("Father")

class Son(Father):
    def show_son(self):
        print("Son")

s = Son()
s.show_grandfather()
s.show_father()
s.show_son()




# Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()




# Hybrid Inheritance
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):
    def show_d(self):
        print("Class D")

d = D()
d.show_a()
d.show_b()
d.show_c()
d.show_d()




