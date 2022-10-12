from random import randint


GAME_BEGINNING = 'Answer "yes" if the number is even, otherwise answer "no"'
FIRST_NUMBER = 1
SECOND_NUMBER = 100


def game_code():
    first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    print('Question: ', first_rand_number)
    if first_rand_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
