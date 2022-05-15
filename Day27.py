"""
Write a function called unique_numbers that takes a list of numbers as an argument. 
Your function is going to find all the unique numbers in the list. It will then sum 
up the unique numbers. You will calculate the difference between the sum of all the 
numbers in the original list and the sum of unique numbers in the list. If the 
difference is an even number, your function should return the original list. If the 
difference is an odd number, your function should return a list with unique numbers 
only. For example [1, 2, 4, 5, 6, 7, 8, 8] should return [1, 2, 4, 5, 6, 7, 8, 8].
"""


def unique_numbers(numbers: list) -> list:
    sum_of_numbers = sum(numbers)
    sum_of_unique_numbers = sum(set(numbers))
    if (sum_of_numbers - sum_of_unique_numbers) % 2 == 0:
        return numbers
    else:
        # return list(set(numbers)) # won't preseve the order of item
        unique_list = list()
        [unique_list.append(x) for x in numbers if x not in unique_list]
        return unique_list


print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))
print(unique_numbers([2, 4, 3, 9, 8, 2, 3]))

