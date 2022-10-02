from brain_games.cli import welcome_user
from random import randint

def parity_check():
  welcome_user()
  name = input()
  print('Answer "yes" if the number is even, otherwise answer "no".')
  #rand_number = randint(0, 100)
  right_answer = ''
  counter = 0


  while counter != 3:
    rand_number = randint(0, 100)
    print('Question: ', rand_number)
    if rand_number % 2 == 0:
      right_answer = 'yes'
    else:
      right_answer = 'no'
  
    ur_answer = input()
    end_of_game = f'{ur_answer} is wrong answer ;(. Correct answer was {right_answer}.\nLet\'s try again, {name}\''
    if ur_answer == right_answer:
      counter += 1
      print('Correct!')
    else:
      print(end_of_game)
      break
    if counter == 3:
      print(f'Congratulations, {name}!')
