"""
Day 17: User Name Generator
Write a function called user_name, that creates a username for the user. The function
should ask a user to input their name. The function should then reverse the name and 
attach a randomly issued number between 0 – 9 at the end of the name. The function 
should return the username.
"""
from random import choice

number = '0123456789'


def user_name():
    user_name_generated = ''.join(reversed(input("Enter your name: ")))
    return user_name_generated + choice(number)


print(user_name())