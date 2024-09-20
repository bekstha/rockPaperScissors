import random

print(("Welcome to the rock, paper, scissors game."))

# win counts
user_wins = 0
computer_wins = 0

# list
options = ["rock", "paper", "scissors"]

# while loop
while True:
    user_input = input("Type rock, paper or scissors. If you wish to quit please enter 'q'. ").strip().lower()
    
    # break the loop if user enters 'q'
    if user_input == "q":
        break

    # if user inputs something other than the program intends, continue the loop
    if user_input not in options:
        continue

    # generating random number between 0 to 2
    random_number = random.randint(0,2)
    # associating randomly generated number to the options list
    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    # if-loop to check wins and draws
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

# when the loop ends user is presented with total number of wins.
print("\nYou won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Thank you for playing!!\n")