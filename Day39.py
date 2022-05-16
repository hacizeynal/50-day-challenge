"""
Day 39: Password Generator
Create a function called generate_password that generates any length of password for 
the user. The password should have a random mix of upper letters, lower letters, 
numbers, and punctuation symbols. The function should ask the user how strong they 
want the password to be. The user should pick from - weak, strong, and very strong. 
If the user picks weak, the function should generate a 5 character long password. 
If the user picks strong, generate an 8 character password and if they pick very 
strong, generate a 12 character password.
"""

import random


def generate_random_string(length):
    pw_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*_='
    return ''.join(random.sample(pw_string, length))


def generate_password():
    message = '\n1. weak \n2. strong \n3. very strong\n'
    try:
        final_message = 'Your password is:'
        password_type = int(input(f"How strong password you want to have? {message}"))

        if password_type > 3:
            raise ValueError
        if password_type == 1:
            print(f'{final_message} {generate_random_string(5)}')
        elif password_type == 2:
            print(f'{final_message} {generate_random_string(8)}')
        elif password_type == 3:
            print(f'{final_message} {generate_random_string(12)}')

    except ValueError:
        print('Inavild password type choosen')


generate_password()
