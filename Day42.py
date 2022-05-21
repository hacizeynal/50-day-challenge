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
