"""
Day 16: Sum the List
Write a function called sum_list with one parameter that takes a nested list of 
integers as an argument and returns the sum of the integers. For example, if you pass
[[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.
"""

from Day14 import flat_list


def sum_list(nested_list: list):
    return sum(flat_list(nested_list))


# test
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
