import random
import pyfiglet

print(pyfiglet.figlet_format("Rock, Paper, Scissors"))
print("Welcome to the Rock, Paper, Scissors game!")
print("1. Single Player")
print("2. Two Player")
mode = input("Please choose a mode (1 or 2): ")
if mode not in ["1", "2"]:
    print("Invalid input. Please try again.")
    exit()

print("1.  1")
print("3.  3")
print("5.  5")
rounds = input("Please choose the number of rounds (1, 3, or 5): ")
if rounds not in ["1", "3", "5"]:
    print("Invalid input. Please try again.")
    exit()
rounds = int(rounds)

player1_score = 0
player2_score = 0
while player1_score < rounds and player2_score < rounds:
    player1_choice = input("Player 1, choose rock, paper, or scissors: ").lower()
    if player1_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue
    if mode == "1":
        player2_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {player2_choice}")
    else:
        player2_choice = input("Player 2, choose rock, paper, or scissors: ").lower()
        if player2_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissors" and player2_choice == "paper"):
        print("Player 1 wins this round!")
        player1_score += 1
    else:
        print(f"{'Computer' if mode == '1' else 'Player 2'} wins this round!")
        player2_score += 1

if player1_score > player2_score:
    print(f"Congratulations! {'You' if mode == '1' else 'Player 1'} won the game!")
else:
    print(f"Sorry, {'you' if mode == '1' else 'Player 2'} won the game. Better luck next time!")
