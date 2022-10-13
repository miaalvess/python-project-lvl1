from random import randint, choice


GAME_BEGINNING = 'What is the result of the expression?'
FIRST_NUMBER = 1
SECOND_NUMBER = 50


def game_code():
    first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    second_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
    rand_sign = ['+', '-', '*']
    char = choice(rand_sign)
    empty_str = ''
    question = f'{first_rand_number} {char} {second_rand_number}'
    if char == '+':
        empty_str = eval(f'{first_rand_number} {char} {second_rand_number}')
       # print('Question: 'f'{first_rand_number} {char} {second_rand_number}')
    else:
        empty_str = eval(f'{first_rand_number} {char} {second_rand_number}')
        #print('Question: 'f'{first_rand_number} {char} {second_rand_number}')
    correct_answer = str(empty_str)
    return question, correct_answer
