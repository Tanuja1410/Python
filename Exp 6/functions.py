# simple greet message
def greet():
    print("Hello!")
greet()


# with arguement
def add(a, b):
    print("Sum:", a + b)
add(10, 20)


# with return value
def square(n):
    return n * n
result = square(5)
print("Square:", result)


# with default arguement
def greet(name="Student"):
    print("Hello", name)
greet()
greet("Tanuja")


# find largest elememt
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(20, 10))



