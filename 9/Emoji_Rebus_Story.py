dict = {
  "girl": "👧",
  "mom": "👩",
  "chicken": "🐔",
  "house": "🏠",
  "eggs": "🥚🥚",
  "bus" : "🚌",
  "school": "🏫"
}

text = 'The girl went to the chicken house to get the eggs . The girl took the eggs to her mom . Then she got on the bus to go to school .'
words = text.split()
new_words = []

for word in words :
    if word in dict :
        new_words.append(dict[word])
    else :
        new_words.append(word)

new_text = ' '.join(new_words)

print(new_text)