
# Line plot
import matplotlib.pyplot as plt # type: ignore
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()



#barchart
import matplotlib.pyplot as plt
students = ["A", "B", "C", "D"]
marks = [80, 70, 90, 85]
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()



#histogram
import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 30, 30, 40, 40, 50]
plt.hist(data, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()



#pie chart
import matplotlib.pyplot as plt
subjects = ["Python", "Java", "C", "HTML"]
marks = [30, 25, 20, 25]
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Subject Distribution")
plt.show()


