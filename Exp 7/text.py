
text="Hii Tanuja"
print(text)

print(text.upper())
print(text.lower())

print(text.title())

# find word
print(text.find("Tanuja"))
print("Hii" in text)

# replace word
new_text = text.replace("Hii", "Hello")
print(new_text)

word= text.split
print(word())

# length
print("Number of characters:",len(text))

# count vowel and consonant
vowels = 0
consonants = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

# reverse
text = input("Enter a string: ")
reverse = text[::-1]
print("Reverse:", reverse)

# palindrome





















































