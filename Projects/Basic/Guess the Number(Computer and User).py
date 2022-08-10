import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, too low.")
        elif guess > random_number:
            print("Sorry, guess again, too high.")

    print(f"Yay!, congrats. You have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1  # min
    high = x  # max
    feedback = ""
    guess = 0
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f"is {guess} to high(H), too low(L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Yay!, The computer guess your number, {guess} correctly!")


# user_guess(1000)
# computer_guess(1000)
