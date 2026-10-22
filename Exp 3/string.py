# string length
# user_string = input("Enter a string: ")
# string_length = 0
# for character in user_string:
#     string_length += 1 
# print("The length of the string is:", string_length)





# string count
# user_string = input("Enter a string: ")

# vowels_count = 0
# consonants_count = 0
# digits_count = 0
# spaces_count = 0
# special_count = 0

# vowels_set = "aeiouAEIOU"
# consonants_set = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# for char in user_string:
#     if char in vowels_set: 
#         vowels_count += 1
#     elif char in consonants_set:
#         consonants_count += 1
#     elif char.isdigit():  
#         digits_count += 1
#     elif char.isspace():  
#         spaces_count += 1
#     else:  
        
#         special_count += 1

# print(f"Vowels: {vowels_count}")
# print(f"Consonants: {consonants_count}")
# print(f"Digits: {digits_count}")
# print(f"Spaces: {spaces_count}")
# print(f"Special Characters: {special_count}")





# reverse string
# user_string = input("Enter a string: ")

# reversed_string = user_string[::-1]
# print("Reversed string:", reversed_string)




# palindrome check
# user_string = input("Enter a string: ")
# cleaned_string = user_string.lower()

# reversed_string = cleaned_string[::-1]

# if cleaned_string == reversed_string:
#     print(f"'{user_string}' is a palindrome!")
# else:
#     print(f"'{user_string}' is NOT a palindrome.")





# upper and lower case
# user_string = input("Enter a string: ")

# uppercase_count = 0
# lowercase_count = 0

# for char in user_string:
#     if char.isupper():   
#         uppercase_count += 1
#     elif char.islower(): 
#         lowercase_count += 1

# print(f"Uppercase letters: {uppercase_count}")
# print(f"Lowercase letters: {lowercase_count}")




# replace all characters
# user_string = input("Enter a string: ")
# char_to_replace = input("Enter the character to replace: ")
# new_char = input("Enter the new character: ")

# modified_string = user_string.replace(char_to_replace, new_char)

# print("Modified string:", modified_string)




# remove all spaces
# user_string = input("Enter a string: ")
# no_spaces_string = user_string.replace(" ", "")

# print("String without spaces:", no_spaces_string)




# frequency of character
# user_string = input("Enter a string: ")
# target_char = input("Enter the character to count: ")

# appearance_count = user_string.count(target_char)

# print(f"The character '{target_char}' appears {appearance_count} time(s).")




# first and last character of string
# user_string = input("Enter a string: ")

# if user_string == "":
#     print("The string is empty!")
# else:
#     first_char = user_string[0]
#     last_char = user_string[-1]

#     print("First character:", first_char)
#     print("Last character:", last_char)



#count total no. of words
# user_sentence = input("Enter a sentence: ")
# words_list = user_sentence.split()
# word_count = len(words_list)
# print(f"Total number of words: {word_count}")

 

# total no. of words
# user_sentence = input("Enter a sentence: ")
# words_list = user_sentence.split()
# word_count = len(words_list)
# print(f"Total number of words: {word_count}")



# longest word
user_sentence = input("Enter a sentence: ")
words_list = user_sentence.split()
longest_word = max(words_list, key=len)





