# #search the word
# import re
# text = "Python is easy to learn"
# result = re.search("Python", text)
# if result:
#     print("Word found")
# else:
#     print("Word not found")



# #find 
# import re
# text = "Python is easy. Python is powerful."
# result = re.findall("Python", text)
# print(result)



# #find numbers
# import re
# text = "I have 10 apples and 20 oranges."
# numbers = re.findall(r"\d+", text)
# print(numbers)



# #replace word
# import re 
# text = "My name is Tanuja"
# new_text = re.sub("Tanuja","Tanu",text)
# print(new_text)



# #match
# import re
# text = "Python is easy"
# result = re.match("Python", text)
# if result:
#     print("Pattern matched")
# else:
#     print("Pattern not matched")



# #split
# import re
# text = "Apple,Orange;Banana Mango"
# result = re.split(r"[,; ]", text)
# print(result)    



# #length of digits 
# import re
# text = "My marks are 85 and my roll number is 25."
# digits = re.findall(r"\d", text)
# print("Number of digits:", len(digits))



#validate mobile number 
# import re
# mobile = input("Enter mobile number: ")
# pattern = r"^[6-9]\d{9}$"
# if re.fullmatch(pattern, mobile):
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")


#validate emailid
# import re
# email = input("Enter email: ")
# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# if re.fullmatch(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")


#password
import re
password = input("Enter password: ")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")