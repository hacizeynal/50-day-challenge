"""
Day 9: Biggest Odd Number
Create a function called biggest_odd that takes a string of numbers and returns the 
biggest odd number in the list. For example, if you pass ‘23569’ as an argument, 
your function should return 9. Use list comprehension.
"""


def biggest_odd(numbers: str) -> int:
    return max([int(x) for x in numbers if int(x) % 2 != 0])


# test
print(biggest_odd('23569'))
print(biggest_odd('13547'))
