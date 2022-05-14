"""
Day 8: Odd and Even
Write a function called odd_even that has one parameter and takes a list of numbers 
as an argument. The function returns the difference between the largest even number 
in the list and the smallest odd number in the list. For example, if you pass 
[1,2,4,6] as an argument the function should return 6 -1= 5.
"""


def odd_even(numbers: list) -> list:
    odds, evens = [], []
    [evens.append(x) if x % 2 == 0 else odds.append(x) for x in numbers]
    return max(evens) - min(odds)


# test
print(odd_even([1, 2, 4, 6]))
print(odd_even([-1, 1, 2, 4, 6]))
