"""
Day 6: User Name Generator
Write a function called user_name that generates a username from the user’s email. 
The code should ask the user to input an email and the code should return everything
before the @ sign as their user name. For example, if someone enters ben@gmail.com, 
the code should return ben as their user name
"""


def user_name() -> str:
    try:
        email = input("Enter a Your email: ")
        return email[:email.index('@')]
    except ValueError:
        return "email doesn't contains @ please enter valid email."


print(user_name())
