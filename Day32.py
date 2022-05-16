"""
Day 32: Password Validator
Write a function called password_validator. The function asks the user to enter a 
password. A valid password should have at least one upper letter, one lower letter, 
and one number. It should not be less than 8 characters long. When the user enters a 
password, the function should check if the password is valid. If the password is 
valid, the function should return the valid password. If the password is not valid, 
the function should tell the users the errors in the password and prompt the user to 
enter another password. The code should only stop once the user enters a valid 
password. (use while loop).
"""


# reference: https://www.geeksforgeeks.org/password-validation-in-python/
def constains_valid_char(password_str: str) -> bool:
    if len(password_str) < 8:
        print('Password can\'t be less than of 8 digits.')
        return False
    elif not any(x.isupper() for x in password_str):
        print('password most contains alteast one upper case character.')
        return False
    elif not any(x.isdigit() for x in password_str):
        print('password most contains alteast one digit')
        return False
    elif not any(x.islower() for x in password_str):
        print('Passowrd most contains atleast one lower case character.')
        return False
    else:
        return True


def password_validator() -> str:
    while not constains_valid_char((password := input("\nEnter your password: "))):
        print(f'\nEntered password {password} is not valid.\nPlease Try again!!!')

    return f'\n{password} is valid password.'


print(password_validator())
