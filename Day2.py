"""
Write a function called convert_add that takes a list of 
strings as an argument and converts it to integers and sums the list. 
For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.
"""


def convert_add(numbers):
    return sum([int(i) for i in numbers if i.isdigit()])


assert (convert_add(['1', '3', '5']) == 9),'convert_add failed!!!'


print(convert_add(['1', '3', '5']))
print(convert_add(['2', '8', '10']))
assert (convert_add(['3', 'i', '5']) == 8), 'Assertation error occured'
