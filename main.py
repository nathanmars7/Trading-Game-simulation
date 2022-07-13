import random
print('14th July 2022')
print('Day 1')

print('Project - Trading game simulation /pseudo code')
# create a bag with 10 marbels
bag = ['green']*6 + ['red']*4
# Starting amount of monney
start_purse = 1000
# Current amount of money (ie Balance)
purse = start_purse
# Result of the last round
result = 0
# How many rounds
rounds = 3
# last marble
marble = 'none'
# Welcome the user to the game
print(f'You start the game with {start_purse} gold pieces')
# Loop drawing mables
for draw in range(1, rounds+1):
  # How much was bet
  bet_amount = int(input(
      f'Current purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
  # draw mable
  marble = random.choice(bag)
  # Win or loose
  if marble == 'green':
     result = bet_amount
  else:
     result = -bet_amount
  # Calc win or loss  / new amount/purse
  purse += result
  # conditions
  if purse < 0.5*start_purse:
     print(f'Game over! You lost to much gold!!!')
  # Result
  print(f'purse: {purse}, last result: ({marble}): {result}')
# Final result
print('starting/ ending purse: ', start_purse, '/', purse)
print('gain/loss: ', ((purse-start_purse)/start_purse * 100), '%')
