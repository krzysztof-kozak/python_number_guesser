from replit import clear

from functions import (
    greet_user,
    choose_mode,
    get_number_of_tries,
    get_random_number,
    print_question,
    check_if_correct_answer
    )

GAME_OVER_MESSAGE = "\nGame over, you ran out of guesses!"
GAME_WIN_MESSAGE = "\nThat's right, you guessed it!"


def start_game():
    clear()

    greet_user()
    mode = choose_mode()
    number_of_tries = get_number_of_tries(mode)

    number_to_guess = get_random_number()
    print(f'psst, the answer is {number_to_guess}')

    print_question(number_of_tries)
    player_answer = check_if_correct_answer(number_to_guess, number_of_tries)

    if player_answer:
        print(GAME_WIN_MESSAGE)
    else:
        print(GAME_OVER_MESSAGE)

start_game()
play_again = False


if input("\nGo again? Type y to play or anykey to quit: ").lower() == "y":
    play_again = True
else:
    print("\nGoodbye!")

while play_again:
    start_game()
