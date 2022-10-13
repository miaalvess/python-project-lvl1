from random import randint


GAME_BEGINNING = 'Find the greatest common divisor of given numbers.'
FIRST_NUMBER = 1
SECOND_NUMBER = 50


def game_code():
    first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    second_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    question = f'{first_rand_number} {second_rand_number}'
    while first_rand_number != second_rand_number:
        if first_rand_number > second_rand_number:
            first_rand_number -= second_rand_number
        else:
            second_rand_number -= first_rand_number
    correct_answer = str(first_rand_number)
    return question, correct_answer
