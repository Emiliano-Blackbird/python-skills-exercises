# 21 dice game

import random

print('Welcome to the 21 Dice Game!')
number = 0
while number < 21:
    roll = random.randint(1, 6)
    number += roll
    print(f'You rolled a {roll}. Your total is {number}.')
    if number > 21:
        print('You went over 21! You lose!')
        break
    elif number == 21:
        print('You hit 21! You win!')
        break
    else:
        answer = input('Do you want to roll again? (y/n) ')
        if answer.lower() != 'y':
            print(f'You ended the game with a total of {number}.')
            break
