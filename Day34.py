"""
In this challenge, copy the text below and save it as a CSV file. Save it in the same 
folder as your Python file. Save it as python.csv. Write a function called just_digits
that reads the text from the CSV file and returns only digit elements from the file. 
Your function should return 1991, 2, 200, 3, 2008 as a list of strings.
"""


def just_digits():
    list_of_digits = list()
    with open('python.csv', 'r') as file:
        [list_of_digits.append(x) for line in file.readlines()\
             for x in line.split() if x.isdigit()]
    # return ', '.join(list_of_digits)
    return list_of_digits


print(just_digits())
