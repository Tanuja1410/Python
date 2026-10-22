# 1.	Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# ●	Add a new student and their grade.
# ●	Update the grade of an existing student.
# ●	Remove a student from the list.
# ●	Calculate and display the average grade of the class.
# ●	Display the highest and lowest grades in the class.
# Tasks:
# ●	Use lists to store the student names and their corresponding grades.
# ●	Implement functions to add, update, remove, and calculate the average and extreme grades.


students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added successfully.")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"{name}'s grade updated to {new_grade}.")
    else:
        print("Student not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} removed successfully.")
    else:
        print("Student not found.")

def calculate_average():
    if len(grades) == 0:
        print("No grades available.")
    else:
        average = sum(grades) / len(grades)
        print("Average Grade:", average)

def display_highest_lowest():
    if len(grades) == 0:
        print("No grades available.")
    else:
        highest = max(grades)
        lowest = min(grades)
        print("Highest Grade:", highest)
        print("Lowest Grade:", lowest)

def display_students():
    if len(students) == 0:
        print("No students in the list.")
    else:
        print("\nStudent List")
        for i in range(len(students)):
            print(students[i], "-", grades[i])

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Display Students")
    print("5. Calculate Average Grade")
    print("6. Display Highest and Lowest Grades")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)

    elif choice == "2":
        name = input("Enter student name to update: ")
        new_grade = float(input("Enter new grade: "))
        update_grade(name, new_grade)

    elif choice == "3":
        name = input("Enter student name to remove: ")
        remove_student(name)

    elif choice == "4":
        display_students()

    elif choice == "5":
        calculate_average()

    elif choice == "6":
        display_highest_lowest()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")



# 2.	Write a program to develope a system that manages the positions of points in a 2D plane. The position of each point is represented as a tuple of two values: (x, y). Write a program that:
# ●	Takes a list of points as input.
# ●	Calculates the distance between two given points.
# ●	Finds the point that is farthest from the origin (0, 0).
# Tasks:
# ●	Use tuples to represent the coordinates of each point.
# ●	Implement a function to calculate the Euclidean distance between two points using their tuple representations.
# ●	Implement a function to find the farthest point from the origin.

import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def farthest_from_origin(points):
    farthest_point = points[0]
    max_distance = distance(farthest_point, (0, 0))

    for point in points:
        d = distance(point, (0, 0))
        if d > max_distance:
            max_distance = d
            farthest_point = point

    return farthest_point, max_distance



n = int(input("Enter number of points: "))

points = []


for i in range(n):
    x = float(input(f"Enter x coordinate of point {i + 1}: "))
    y = float(input(f"Enter y coordinate of point {i + 1}: "))
    points.append((x, y))

print("\nPoints:", points)


p1 = tuple(map(float, input("Enter first point (x y): ").split()))
p2 = tuple(map(float, input("Enter second point (x y): ").split()))

print("Distance between points:", distance(p1, p2))


point, d = farthest_from_origin(points)

print("Point farthest from origin:", point)
print("Distance from origin:", d)





# 3.	Write a program to design a configuration system for a web server where some configuration settings should not be changed during runtime, while others can be updated. The server settings are as follows:
# ●	server_ip: A tuple representing the IP address of the server, which should remain unchanged.
# ●	allowed_ips: A list of IP addresses allowed to connect to the server, which can be updated during runtime.
# Write a program that:
# ●	Allows updating the allowed_ips list.
# ●	Prevents updating the server_ip tuple.
# ●	Displays the updated configuration.
# Tasks:
# ●	Use a tuple for server_ip and a list for allowed_ips.
# ●	Implement a function to update allowed_ips but prevent changes to server_ip.


class WebServerConfig:
    def __init__(self, server_ip, allowed_ips):
        self._server_ip = tuple(server_ip)
        self.allowed_ips = list(allowed_ips)

    @property
    def server_ip(self):
        return self._server_ip

    def add_allowed_ip(self, ip):
        if ip not in self.allowed_ips:
            self.allowed_ips.append(ip)

    def remove_allowed_ip(self, ip):
        if ip in self.allowed_ips:
            self.allowed_ips.remove(ip)

    def update_server_ip(self, new_ip):
        try:
            self.server_ip = new_ip
        except AttributeError:
            print("Action Denied: 'server_ip' is immutable and cannot be updated.")

    def display_config(self):
        print(f"Server IP (Immutable): {self.server_ip}")
        print(f"Allowed IPs (Mutable)  : {self.allowed_ips}")


config = WebServerConfig((192, 168, 1, 100), ["192.168.1.10", "192.168.1.20"])

print("--- Initial Configuration ---")
config.display_config()

print("\n--- Updating Allowed IPs ---")
config.add_allowed_ip("192.168.1.30")
config.display_config()

print("\n--- Attempting to Update Server IP ---")
config.update_server_ip((10, 0, 0, 1))

print("\n--- Final Configuration ---")
config.display_config()





#  4.	Write a program to manage two different projects in your company, and you need to analyze employee involvement. The employees working on each project are represented as sets. Write a program that:
# ●	Displays the employees working on both projects (intersection).
# ●	Displays the employees working only on one project (difference).
# ●	Displays the total unique employees across both projects (union).
# Tasks:
# ●	Use sets to represent the employees in each project.
# ●	Perform union, intersection, and difference operations to analyze employee involvement.
       
def analyze_employee_involvement(project_a, project_b):
    both_projects = project_a.intersection(project_b)
    
    only_project_a = project_a.difference(project_b)
    only_project_b = project_b.difference(project_a)
    
    only_one_project = project_a.symmetric_difference(project_b)
    
    all_unique_employees = project_a.union(project_b)
    
    print("=== Employee Project Analysis ===")
    print(f"Project A Employees: {project_a}")
    print(f"Project B Employees: {project_b}")
    print("-" * 40)
    
    print(f"1. Working on BOTH projects (Intersection): {both_projects}")
    print(f"2. Working ONLY on Project A (Difference): {only_project_a}")
    print(f"3. Working ONLY on Project B (Difference): {only_project_b}")
    print(f"   Working ONLY on one project (Symmetric Difference): {only_one_project}")
    print(f"4. Total unique employees across both projects (Union): {all_unique_employees}")

project_alpha = {"Alice", "Bob", "Charlie", "David", "Eve"}
project_beta = {"Charlie", "Eve", "Frank", "Grace", "Heidi"}

analyze_employee_involvement(project_alpha, project_beta)





# 5.	Write a program to build a simple text analysis tool. The tool should perform the following operations on a given paragraph of text:
# ●	Count the total number of words.
# ●	Count the frequency of each word.
# ●	Identify and display the top 3 most frequent words.
# ●	Count the number of vowels in the entire text.
# Tasks:
# ●	Use string manipulation to split the text into words and to check for vowels.
# ●	Use a dictionary to store the word frequencies.

import string
from collections import Counter

def analyze_text(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    
    words = cleaned_text.split()
    total_words = len(words)
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
      
    top_3_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:3]

    print("=== Text Analysis Results ===")
    print(f"Total Words: {total_words}")
    print(f"Total Vowels: {vowel_count}\n")
    
    print("--- Top 3 Most Frequent Words ---")
    for word, count in top_3_words:
        print(f"'{word}': {count} time(s)")
        
    print("\n--- All Word Frequencies ---")
    for word, count in word_freq.items():
        print(f"'{word}': {count}")

sample_paragraph = """
Python is an amazing programming language. Python is flexible, powerful, 
and easy to learn. Learning Python opens up many opportunities in data 
science and software development.
"""
analyze_text(sample_paragraph)





# 6.	Write a program to analyze the vocabulary used in two different books. You need to:
# ●	Find all unique words used in each book.
# ●	Identify the common words between both books.
# ●	Identify words that are unique to each book (not found in the other book).
# ●	Display the total number of unique words across both books.
# Tasks:
# ●	Use sets to find the unique words in each text, and perform set operations to find the union, intersection, and differences.

import string

def extract_unique_words(text):
    # Remove punctuation and convert text to lowercase
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    # Return unique words as a set
    return set(cleaned_text.split())

def analyze_vocabularies(book1_text, book2_text):
    # Get unique words for each book
    book1_words = extract_unique_words(book1_text)
    book2_words = extract_unique_words(book2_text)
    
    # Set Operations
    common_words = book1_words.intersection(book2_words)
    only_book1 = book1_words.difference(book2_words)
    only_book2 = book2_words.difference(book1_words)
    total_unique_words = book1_words.union(book2_words)
    
    # Display Results
    print("=== Vocabulary Analysis Results ===")
    print(f"Unique words in Book 1 ({len(book1_words)} words): {book1_words}")
    print(f"Unique words in Book 2 ({len(book2_words)} words): {book2_words}")
    print("-" * 50)
    
    print(f"1. Common words in both books (Intersection - {len(common_words)} words):")
    print(f"   {common_words}\n")
    
    print(f"2. Words UNIQUE to Book 1 (Difference - {len(only_book1)} words):")
    print(f"   {only_book1}\n")
    
    print(f"3. Words UNIQUE to Book 2 (Difference - {len(only_book2)} words):")
    print(f"   {only_book2}\n")
    
    print(f"4. Total unique words across BOTH books (Union - {len(total_unique_words)} words):")
    print(f"   {total_unique_words}")

# Sample texts representing two books
book_1 = """
The old man sat by the sea. He watched the waves crash against the shore.
The quiet sea was full of secrets.
"""

book_2 = """
The young girl explored the deep forest. She heard the birds singing in the trees.
The quiet forest was full of wonder.
"""

analyze_vocabularies(book_1, book_2)