from random import randint

GAME_BEGINNING = 'What number is missing in the progression?'
FIRST_NUMBER = 1
SECOND_NUMBER = 10
THIRD_NUMBER = 45
FOURTH_NUMBER = 70

FIRST_HIDEN_NUMBER = 0
SECOND_HIDEN_NUMBER = 10

STEP_START = 3
STEP_END = 5


def game_code():
    hiden_number = randint(FIRST_HIDEN_NUMBER, SECOND_HIDEN_NUMBER)
    progression_lenth = 10
    empty_list = []
    counter_in_game = 0
    while counter_in_game != 1:
        first_rand_number = randint(FIRST_NUMBER, SECOND_NUMBER)
        second_rand_number = randint(THIRD_NUMBER, FOURTH_NUMBER)
        step = randint(STEP_START, STEP_END)
        rand_nums_range = range(first_rand_number, second_rand_number, step)
        for i in rand_nums_range:
            empty_list.append(i)
            if len(empty_list) == progression_lenth:
                counter_in_game += 1
                break
    hiden_number_finding = (len(empty_list) - 1) - hiden_number
    correct_answer = str(empty_list[hiden_number_finding])
    empty_list[hiden_number_finding] = '..'
    empty_string = ''
    for _ in empty_list:
        empty_string += str(_) + ' '
    question = f'{empty_string}'
    return question, correct_answer
