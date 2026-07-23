# Simple Python examples collection
import sys
import urllib.request


def hello_world():
    print("Hello, world!")


def sum_demo(a, b):
    print(f"Sum: {a + b}")


def sum_interactive():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)


def fib(n):
    a, b = 0, 1
    vals = []
    for _ in range(n):
        vals.append(a)
        a, b = b, a + b
    return vals


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


def read_write_file():
    name = "sample.txt"
    with open(name, "w", encoding="utf-8") as f:
        f.write("Hello file\n")
    with open(name, encoding="utf-8") as f:
        print(f"Contents of {name}:")
        print(f.read())


def http_get(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = r.read().decode(errors='replace')
        print(f"Fetched {len(data)} bytes from {url}")
    except Exception as e:
        print("HTTP GET failed:", e)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"


def demo():
    print('\n--- Demo: Simple Python Examples ---')
    hello_world()
    sum_demo(2, 3)
    print('Fibonacci(10):', fib(10))
    print('Factorial(5):', factorial(5))
    print("Is palindrome?", is_palindrome("A man, a plan, a canal: Panama"))
    read_write_file()
    http_get('https://httpbin.org/get')
    p = Person('Ada')
    print(p.greet())
    print('--- Demo complete ---\n')


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'demo':
        demo()
        return

    while True:
        print('\nChoose an example to run:')
        print('1) Hello world')
        print('2) Sum (interactive)')
        print('3) Fibonacci (print first 10)')
        print('4) Factorial (5)')
        print('5) Palindrome test')
        print('6) Read/Write file')
        print('7) HTTP GET (https://httpbin.org/get)')
        print('8) Person class')
        print('9) Run demo')
        print('0) Exit')
        choice = input('> ').strip()
        if choice == '1':
            hello_world()
        elif choice == '2':
            sum_interactive()
        elif choice == '3':
            print(fib(10))
        elif choice == '4':
            print(factorial(5))
        elif choice == '5':
            s = input('Enter text: ')
            print(is_palindrome(s))
        elif choice == '6':
            read_write_file()
        elif choice == '7':
            url = input('URL (default https://httpbin.org/get): ').strip() or 'https://httpbin.org/get'
            http_get(url)
        elif choice == '8':
            name = input('Name: ').strip() or 'Anonymous'
            print(Person(name).greet())
        elif choice == '9':
            demo()
        elif choice == '0':
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
