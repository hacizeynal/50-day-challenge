"""
Day 3: Register Check
Write a function called register_check that checks how many students are in school. 
The function takes a dictionary as a parameter. If the student is in school, the 
dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. 
Your function should return the number of students in school. Use the dictionary 
below. Your function should return 3.
register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
"""


def register_check(registers: dict) -> int:
    present = 0
    for i, j in registers.items():
        if registers[i].lower() == 'yes':
            present += 1
    return present


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(registers=register))
