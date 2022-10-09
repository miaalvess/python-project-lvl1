from random import randint
import prompt



def parity_check():
  name = prompt.string('May I have your name? ')
  print('Hello,',name, end='! \n')
  print('Answer "yes" if the number is even, otherwise answer "no".')
  #name = input()
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
