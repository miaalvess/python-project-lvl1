from random import randint


GAME_BEGINNING = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_NUMBER = 1
SECOND_NUMBER = 500


def game_code():
    first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    question = f'{first_rand_number}'
    correct_answer = ''
    for i in range(2, int(first_rand_number ** 0.5) + 1):
        if first_rand_number % i == 0:
            correct_answer = "no"
            break
        correct_answer = 'yes'
    return question, correct_answer
