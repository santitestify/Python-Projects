import random


choices = ["rock", "paper", "scissors"]

# computer = input("Choice rock, paper or scissors: ")
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("Choice rock, paper or scissors: ").lower()  # sea mayuscula o miniscula

    if player == choices[0] and computer == choices[1]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("Computer wins")
    elif player == choices[1] and computer == choices[2]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("computer wins")
    elif player == choices[2] and computer == choices[0]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("computer wins")
    elif computer == choices[0] and player == choices[1]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("player wins")
    elif computer == choices[1] and player == choices[2]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("player wins")
    elif computer == choices[2] and player == choices[0]:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("player wins")
    elif computer == player:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("this is a tie!!")


print("bye")

