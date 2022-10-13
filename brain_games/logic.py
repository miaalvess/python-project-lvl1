import prompt


ROUNDS = 3


def logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name} !')
    print(game.GAME_BEGINNING)
    counter = 0
    while counter != ROUNDS:
        question, correct_answer = game.game_code()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        end_of_the_game = f'{your_answer} is wrong answer ;(.'
        end_of_the_game_plus = f"Correct answer was {correct_answer}.\n"
        end = f"Let's try again, {name}!"
        if your_answer == str(correct_answer):
            counter += 1
            print('Correct!')
        else:
            print(end_of_the_game, end_of_the_game_plus, end)
            break
        if counter == 3:
            print(f'Congratulations, {name} !')
