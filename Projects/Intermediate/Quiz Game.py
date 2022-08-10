# ------------------------------------------------------
def new_game():
    guesses = []  # lista de respuestas
    correct_guesses = 0  # contador de respuestas correctas
    question_num = 1  # contador de cada pregunta
    for key in questions:  # muestra las preguntas
        print("#------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:  # muestra las opciones # [question_num] solo si question_num vale 0
            print(i)
        guess = input("Enter (A, B, C or D): ")  # respuesta del usuario
        guess = guess.upper()  # por si ingresa mayuscula
        guesses.append(guess)  # agregar las respuestas a la lista de respuestas

        correct_guesses += check_answer(questions.get(key), guess)  # respuestas correctas key=quest and value=guess

        question_num += 1  # incrementa el numero de opciones
    display_score(correct_guesses, guesses)
# ------------------------------------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

# ------------------------------------------------------


def display_score(correct_guesses, guesses):
    print("#------------------------------------------------------")
    print("Results: ")
    print("#------------------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")

    print("\nGuesses: ", end="")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guesses/len(questions))*100)  # porcentaje de respuestas correctas
    print(f"\nYour score is : % {score}")


questions = {
 "Who created Python?: ": "A",
 "What year was Python created? ": "B",
 "Python is tributed to which comedy group? ": "C",
 "Is the earth round: ": "A"
}

options = [["A. Guido Van rossum", "B. Elon musk", "C. Bill Gates", "D- Mark Zuckerburg "],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smash", "C. Monty Python", "D. SNL"],
          ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

#while play_again():
    # new_game()

print("Bye")