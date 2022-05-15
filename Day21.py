"""
Day 21: List of Tuples
Write a function called make_tuples that takes two lists, equal lists, and combines 
them into a list of tuples. For example if list a is [1,2,3,4] and list b is 
[5,6,7,8], your function should return [(1,5),(2,6),(3,7),(4,8)].
"""


def make_tuples(list_one: list, list_two: list) -> list:
    return (list(zip(list_one, list_two)))


def make_tuples_one(list_one: list, list_two: list) -> list:
    tupled_list = []
    if len(list_one) != len(list_two):
        raise TypeError("Lenght of both lists must be equal.")
    else:
        for i in range(len(list_one)):
            tupled_list.append((list_one[i], list_two[i]))
    return tupled_list


print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8, 9]))  # won't raise error
print(make_tuples([1, 2, 3, 4, 10], [5, 6, 7, 8]))
print(make_tuples_one([1, 2, 3, 4], [5, 6, 7, 8]))
print(make_tuples_one([1, 2, 3, 4], [5, 6, 7, 8, 9]))  # will raise eror
