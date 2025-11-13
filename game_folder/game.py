print("Welcome to Rock-Paper-Scissors!")
while True:
    user_input = input("Choose rock, paper, or scissors: ").lower()
    if user_input in ["rock", "paper", "scissors"]:
        print("You chose:", user_input)
        break
    else:
        print("Your input was invalid.")
        pass