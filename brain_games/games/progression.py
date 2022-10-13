from random import randint

GAME_BEGINNING = 'What number is missing in the progression?'
FIRST_NUMBER = 1
SECOND_NUMBER = 50
THIRD_NUMBER = 75
FOURTH_NUMBER = 100
FIRST_HIDEN_NUMBER = 0
FIRST_HIDEN_NUMBER = 7
STEP_START = 1
STEP_END = 7


def game_code():
    hiden_number = randint(FIRST_HIDEN_NUMBER, FIRST_HIDEN_NUMBER)
    progression_lenth = 8
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
