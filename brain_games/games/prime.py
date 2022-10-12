from random import randint


GAME_BEGINNING = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_NUMBER = 1
SECOND_NUMBER = 500


def game_code():
    first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    print(f'Question:  {first_rand_number}')
    if first_rand_number % 2 != 0 or first_rand_number == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
