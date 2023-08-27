word = input("Enter a word: ")
vowels = "aeiouAEIOU"
new_word = ""
for char in word:
    if char in vowels:
        new_word += "!"
    else:
        new_word += char
print(new_word)
