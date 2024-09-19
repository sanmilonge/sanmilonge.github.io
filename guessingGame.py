from random import randint
from time import sleep
import fp_func_file as fp

possible_options = list(range(101))
winning_number = randint(0, 100)
fp.type_like_effect('Please enter your name: ', delay=0.1)
name = input()
fp.type_like_effect(f'Welcome {name}!', delay = 0.1)
sleep(1)
fp.type_like_effect('\nGuess the lucky number and win the prize!', delay=0.1)
sleep(1)
fp.type_like_effect('\nClue: The number is between 0 and 100...', delay=0.1)
sleep(0.5)
fp.type_like_effect('\nYou have 7 tries.', delay=0.1)
sleep(0.5)
fp.type_like_effect('\nGood luck!😁', delay=0.1)
sleep(2)
counter = 7
previous_guesses = []
while counter >= 1:
    fp.type_like_effect('\nEnter number: ', delay = 0.1)
    try:
        number = int(input())
        if number in previous_guesses:
            counter  -= 1
            fp.type_like_effect(f'You already guessed this number👎!\nTries left: {counter}', delay=0.1)
            continue
        previous_guesses.append(number)
        if number in possible_options:
            if number == winning_number:
                fp.type_like_effect(f'\nCongratulations {name}👍! You guessed the right number!', delay=0.1)
                fp.type_like_effect(f'\nYou guessed the number in {7-counter} tries.', delay=0.1)
                break
            else:
                if number > winning_number:
                    counter -= 1
                    if counter == 0:
                        fp.type_like_effect(f'\nYou have no tries left!', delay=0.1)
                        fp.type_like_effect(f'\nThe winning number was {winning_number}.', delay=0.1)
                        break
                    else:
                        fp.type_like_effect(f'Number is too high👎\nTries left: {counter}', delay = 0.1)
                        continue
            
                if number < winning_number:
                    counter -= 1
                    if counter == 0:
                        fp.type_like_effect(f'\nYou have no tries left!', delay=0.1)
                        fp.type_like_effect(f'\nThe winning number was {winning_number}.', delay=0.1)
                        sleep(1)
                        break
                    else:
                        fp.type_like_effect(f'Number is too low👎\nTries left: {counter}', delay = 0.1)
                        continue
        else:
            fp.type_like_effect('Number is out of range👎!', delay=0.1)
            counter -= 1
            fp.type_like_effect(f'\nYou have {counter} tries left.', delay=0.1)
    except ValueError:
        fp.type_like_effect('Invalid input!', delay=0.1)
        counter -= 1
        fp.type_like_effect(f'\nYou have {counter} tries left.', delay=0.1)
        

