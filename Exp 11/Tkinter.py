# import tkinter as tk

# root = tk.Tk()
# root.title("My First Window")
# root.geometry("400x300")

# root.mainloop()



#Label 
# import tkinter as tk
# root = tk.Tk()
# root.title("Label Example")
# root.geometry("400x300")
# label = tk.Label(root, text="Hello Python!")
# label.pack()
# root.mainloop()



# button
# import tkinter as tk
# def click():
#     print("Button Clicked!")
# root = tk.Tk()
# root.geometry("400x300")
# button = tk.Button(root, text="Click Me", command=click)
# button.pack()
# root.mainloop()


# input and button
# import tkinter as tk

# def show():
#     label.config(text="Hello " + entry.get())

# root = tk.Tk()
# root.geometry("400x300")
# entry = tk.Entry(root)
# entry.pack()

# button = tk.Button(root, text="Submit", command=show)
# button.pack()

# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()





# text input
# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")
# entry = tk.Entry(root)
# entry.pack()

# root.mainloop()





# radiobutton
# import tkinter as tk

# root = tk.Tk()
# root.title("Radiobutton Example")
# root.geometry("300x200")

# gender = tk.StringVar(value="Male")

# tk.Label(root, text="Select Gender").pack()

# tk.Radiobutton(root, text="Male", variable=gender,
#                value="Male").pack()

# tk.Radiobutton(root, text="Female", variable=gender,
#                value="Female").pack()

# def show():
#     label.config(text="Selected: " + gender.get())

# tk.Button(root, text="Submit", command=show).pack()

# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()





# listbox
import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "JavaScript")

root.mainloop()