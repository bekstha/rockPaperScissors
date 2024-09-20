import random

print(("Welcome to the rock, paper, scissors game."))

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock, paper or scissors. If you wish to quit please enter 'q'. ").strip().lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("That's a draw.")
    else:
        print("You lost!")
        computer_wins += 1

print("\nYou won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Thank you for playing!!\n")