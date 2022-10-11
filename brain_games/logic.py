import prompt


ROUNDS = 3


def logic(game):
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name} !')
	print(game.GAME_BEGINNING)
	counter = 0
	while counter != ROUNDS:
		correct_answer = game.game_code()
		your_answer = prompt.string('Your answer: ')
		end_of_game = f'{your_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet\'s try again, \''
		if your_answer == str(correct_answer):
			counter += 1
			print('Correct!')
		else:
			print(end_of_game)
			break
		if counter == 3:
			print(f'Congratulations, {name} !')
