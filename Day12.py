"""
Write a function called count_dots. This function takes a string separated by dots as
 a parameter and counts how many dots are in the string. For example, ‘h.e.l.p.’ 
 should return 4 dots, and ‘he.lp.’ should return 2 dots.
Extra Challenge: Your Age in Minutes
b. Write a function called age_in_minutes that tells a user how old they are in 
minutes. Your code should ask the user to enter their year of birth, and it should 
return their age in minutes (by subtracting their year of birth to the current year).
 Here are things to look out for:
a. The user can only input a 4 digit year of birth. For example, 1930 is a valid year
. However, entering any number longer or less than 4 digits long should render input 
invalid. Notify the user to input a four digits number.
b. If a user enters a year before 1900, your code should tell the user that input is 
invalid. If the user enters the year after the current year, the code should tell the
 user, to input a valid year.
The code should run until the user inputs a valid year. Your function should return 
the user's age in minutes. For example, if someone enters 1930, as their year of birth
 your function should return:
You are 48,355,200 minutes old.

"""

from datetime import date

# problem1


def count_dots(str1: str) -> int:
    return str1.count('.')


# tests
print(count_dots('h.e.l.p.'))
print(count_dots('hel.lp.'))

# problem2


def is_valid_birth_year(birth_year: int) -> bool:
    if birth_year < 1000:
        print('Birth year can\'t be of 3 digit')
        return False
    elif birth_year <= 1900 > 1000:
        print("please enter year greater than 1900")
        return False
    elif birth_year > date.today().year:
        print('Birth year can\'t be in future')
        return False
    return True


def age_in_minutes():
    birth_year = int(input("Enter your birth year: "))
    while not is_valid_birth_year(birth_year):
        birth_year = int(input("\nEnter valid birth year again: "))
    age_in_min = f"{(date.today().year - birth_year)*365*24*60:,}"

    return f'Your are {age_in_min} minutes old.'


print(age_in_minutes())
