from random import choice
from art import logo

GAME_TITLE = "Number Guesser"
EASY_MODE = "easy"
HARD_MODE = "hard"

HINT_HIGHER = "\nToo low, try a higher number."
HINT_LOWER = "\nToo high, try a lower number."




def choose_mode():
    '''Returns string 'easy' or string 'hard'.
       Takes no arguments.
    '''
    valid_answer = False

    while not valid_answer:
        answer = input(f"Choose mode: {EASY_MODE} or {HARD_MODE}: ")

        if answer.lower() in [EASY_MODE, HARD_MODE]:
            valid_answer = True
            return answer
        else:
            print(f"\nInvalid answer, type {EASY_MODE} or {HARD_MODE}.")


def get_number_of_tries(mode):
    '''Returns int 5 or int 10 depeding on the argument passed
       Valid arguments are string 'easy' or str 'hard'.
    '''
    if mode == EASY_MODE:
        return 10
    elif mode == HARD_MODE:
        return 5


def get_random_number():
    '''Returns a random int between 1 and 100 inclusive.'''
    return choice(range(1, 101))


def greet_user():
    '''Prints a logo and a predefined welcome message.'''
    print(logo)
    print(f"Welcome to {GAME_TITLE}")


def print_question(number_of_tries):
    '''Prints a question on screen.
       Does not return anything.
    '''
    print("\nI am thinking of a number between 1 and 100...")
    print(f"Can you guess it in {number_of_tries} tries?\n")


def get_player_answer():
    '''Returns an integer based on player input'''

    valid_answer = False

    while not valid_answer:
        answer = input("My guess is: ")

        if answer.isdigit() and int(answer) in range(1, 101):
            valid_answer = True
            return int(answer)
        else:
            print("\nInvalid answer, type w whole number from 1 to 100")

def check_if_correct_answer(number_to_guess ,number_of_tries):
    '''Returns bool True or False.'''
    has_guessed_correctly = False

    while not has_guessed_correctly:
        number_of_tries -= 1
        player_guess = get_player_answer()

        if number_of_tries < 1:
            return False

        elif player_guess == number_to_guess:
            has_guessed_correctly = True
            return True

        elif player_guess > number_to_guess:
            print(HINT_LOWER)

        elif player_guess < number_to_guess:
            print(HINT_HIGHER)

        print(f"\nTries remaining: {number_of_tries}")