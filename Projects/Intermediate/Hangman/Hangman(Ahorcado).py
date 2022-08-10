import random
from Words import Words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while "-" in word or " " in word:
        word = random.choice(word)
    return word.upper()


def hangman():
    word = get_valid_word(Words)  # Words imported
    word_letters = set(word)  # Conjunct of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Conjunct what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # ' '.join(['a', 'b', 'cd')] --> 'a b cd'
        print(f"You have {lives} lives left and you used these letters: ", ' '.join(used_letters))  # letters used

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life is wrong
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")

    # get here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(f"You died. sorry. the word was {word}")
    else:
        print(f"You guessed the word {word}!!")


hangman()

