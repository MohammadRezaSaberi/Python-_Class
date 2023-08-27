import random
from termcolor import colored

categories = {
    "1 . Animals": ["cat", "dog", "elephant", "giraffe", "lion", "monkey", "panda", "penguin", "tiger", "zebra"],
    "2 . Fruits": ["apple", "banana", "cherry", "grapefruit", "kiwi", "lemon", "mango", "orange", "peach", "watermelon"],
    "3 . Countries": ["australia", "brazil", "canada", "china", "france", "germany", "india", "japan", "russia", "united states"],
    "4 . Sports": ["basketball", "cricket", "football", "golf", "hockey", "rugby", "skiing", "swimming", "tennis", "volleyball"],
    "5 . Colors": ["black", "blue", "green", "orange", "pink", "purple", "red", "white", "yellow"]
}

def play_hangman():
    print("Welcome to Hangman!")
    print("Choose a category:")
    for category in (categories):
        print(category)
    category_choice = int(input("Enter the category you want to play: "))
    category = [category_choice]
    word = random.choice([category])
    guessed_letters = set()
    correct_letters = set()
    incorrect_letters = set()
    attempts_left = 6
    while attempts_left > 0:
        print("\n" + "-" * 20)
        print(f"Category: {category}")
        print(f"Attempts left: {colored(' ❤️ ' * attempts_left, 'red')}")
        display_word = "".join([c if c in correct_letters else "_" for c in word])
        print(f"Word: {display_word}")
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print(colored(f"You already guessed the letter '{guess}'. Try again.", 'red'))
            continue
        guessed_letters.add(guess)
        if guess in word:
            correct_letters.add(guess)
            print(colored(f"Correct! The letter '{guess}' is in the word.", 'green'))
            if len(correct_letters) == len(set(word)):
                print(colored("\nCongratulations! You won!", 'green'))
                return
        else:
            incorrect_letters.add(guess)
            attempts_left -= 1
            print(colored(f"Incorrect. The letter '{guess}' is not in the word.", 'red'))
    print(colored("\nSorry, you lost. Better luck next time!", 'red'))

play_hangman()
