from random import randint, choice


def calc_game():
  #counter = 0
   print('What is the result of the expression?')
  #while counter != 3 :

   first_rand_number = randint(1, 100)
   second_rand_number = randint(1, 100)
   rand_sign = ['+', '-', '*']
   char = choice(rand_sign)
   print('Question: 'f'{first_rand_number} {char} {second_rand_number}')
   empty_str = ''

# тут сама игра 
   if char == '+':
       empty_str = eval(f'{first_rand_number} {char} {second_rand_number}')
   else:
       empty_str = eval(f'{first_rand_number} {char} {second_rand_number}')
   correct_answer = str(empty_str) 
# пиздец все под один стандарт придется делать((((
    ###соответсвенно что ниже идет в логику


   ''' ur_answer = input()
    end_of_game = f'{ur_answer} is wrong answer ;(. Correct answer was {empty_str}.\nLet\'s try again, \''
    if ur_answer == str(empty_str):
      counter += 1
      print('Correct!')
    else:
      print(end_of_game) 
      break
    if counter == 3:
      print('Congratulations, !')'''

