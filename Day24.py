"""
Day 24: Average Calories
Create a function called average_calories that calculates the average calories intake
of a user. The function should ask the user to input their calories intake for any 
number of days and once they hit ‘done’ it should calculate and return the average 
intake.
"""


def average_calories():
    calories = []
    while (user_input := input("enter a calories intake when complete enter done: "))!='done':
        try:
            calories.append(float(user_input))
        except ValueError:
            print('Please enter a valid calories value')
    return f'{sum(calories)/len(calories):.2f}'

print(average_calories())
