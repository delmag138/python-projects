# rock, paper, scissors game
# import the random module
import random

choices = ("rock", "paper", "scissors")

num = 5
while num > 0:
    comp_guess = random.choice(choices)
    user_guess = input("Rock, Paper, Scissors:").lower()
    if user_guess not in choices:
        print("Inavlid input!")
        continue
    if comp_guess == user_guess:
        print("It's a tie!")
    elif (user_guess == "rock" and comp_guess == "scissors") or \
         (user_guess == "paper" and comp_guess == "rock") or \
         (user_guess == "scissors" and comp_guess == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    num -= 1

print("\nGame Over!")
