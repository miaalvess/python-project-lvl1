import prompt
#from brain_games.games.cli import welcome_user


def logic(game): # внутри функции должна находится игра 
  
 
# welcome_user() # модуль приветствия импортируем из cli.py
  name = prompt.string('May I have your name? ')
  counter = 0
  while counter != 3: # не понятно как уместить цикл вайл тут 
    
    correct_answer = game.correct_answer  # непонятно как имопртировать игру как функцию, ведь логику мы используем многократно 

    ur_answer = input() 
    end_of_game = f'{ur_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet\'s try again, {name}\'' # код обоснованно ругается на ввод ответа, тк его нет и думаю код без этого не заработает
    if ur_answer == correct_answer:
      counter += 1
      print('Correct!')
    else:
      print(end_of_game) 
      break
    if counter == 3:
      print(f'Congratulations, {name}!')
  
