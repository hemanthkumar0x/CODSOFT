import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == "exit":
        break
    if user_choice not in choices:
        print("Invalid choice, Try Again.")
        continue

    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        print("YOU WIN!")
    else:
        print("COMPUTER WINS!")
