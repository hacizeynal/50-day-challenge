'''
Day 42: Spelling Checker
Write a function called spelling_checker. This code asks the user to input a word and
if a user inputs a wrong spelling it should suggest the correct spelling by asking 
the user if they meant to type that word. If the user says no, it should ask the 
user to enter the word again. If the user says yes, it should return the correct 
word. If the word entered by the user is correctly spelled the function should return
the correct word. Use the module textblob.
from textblob import Word
'''
from textblob import Word
# step 0 make a function called spelling_checker


def spelling_checker():
    while True:
        # step 1 ask user input
        user_input = Word(input('Enter a word: '))
        result = user_input.correct()
        if user_input != result:
            # step 2 if wrong suggest the user correct spelling
            print(f'The Corect word is {result}.')
            if (would_like_to_update := input("Do you like to update?Y/N ").lower()) == 'y':
                print(f'the correct word is {user_input.correct()}')
                break
            else:
                print('Please try again!!!')
        elif user_input == user_input.correct():
            break

    return f'Your input is: {result}.'


print(spelling_checker())
