"""
Day 38: Guess a Number
Write a function called guess_a_number. The function should ask a user to guess a 
randomly generated number. If the user guesses a higher number, the code should tell 
them that the guess is too high, if the user guesses low, the code should tell them 
that their guess is too low. The user should get a maximum of three guesses. When the
user guesses right, the code should declare them a winner. After three wrong guesses,
the code should declare them a loser.
"""

import random


def guess_a_number():
    print('***GUESSING GAME***')
    random_number = random.randrange(0, 10)  # generate number between
    total_chances = 3
    while total_chances:
        guess = int(input(f"You've {total_chances} {'chance'if total_chances==1 else 'chances'} Enter your guess: "))

        if guess == random_number:
            print('You guessed it right!!!')
            break
        elif guess > random_number:
            print(f'your guess {guess} is higher than actual number.')
        elif guess < random_number:
            print(f'your guess {guess} is lesser than actual number.')

        total_chances -= 1
    else:
        print(f"You miss all the chances correct number is {random_number}.")


guess_a_number()
