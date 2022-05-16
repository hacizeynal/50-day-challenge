"""
Day 33: List Intersection
Write a function called inter_section that takes two lists and finds the intersection 
(the elements that are present in both lists). The function should return a tuple of 
intersections. Use list comprehension in your solution. Use the lists below. 
Your function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85] list2 = [ 42, 30, 80, 65, 68, 88, 95]
Extra Challenge: Set or list
You want to implement a code that will search for a number in a range. You have a 
decision to make as to whether to store the number in a set or a list. Your decision 
will be based on time. You have to pick a data type that executes faster.
You have a range and you can either store it in a set or a list depending on which 
one executes faster when you are searching for a number in the range. See below:
a = range(10000000) x = set(a)
y = list(a)
Let’s say you are looking for a number 9999999 in the range above. Search for this 
number in the list and the set. Your challenge is to find which code executes faster. 
You will pick the one that executes quicker, lists, or sets. Run the two searches and
time them.
"""
from datetime import datetime


def inter_section(list_one: list, list_two: list) -> tuple:
    return sorted(set(list_one).intersection(set(list_two)))


print(inter_section([20, 30, 60, 65, 75, 80, 85],
      [42, 30, 80, 65, 68, 88, 95]))

a = range(10000000)


def list_search(number_to_search: int):
    x = list(a)
    start_time = datetime.today().timestamp()
    for i in x:
        if number_to_search == x:
            break
    finish_time = datetime.today().timestamp()

    return start_time - finish_time


def set_search(number_to_search: int):
    x = set(a)
    start_time = datetime.today().timestamp()
    for i in x:
        if number_to_search == x:
            break
    finish_time = datetime.today().timestamp()

    return start_time - finish_time


if __name__ == '__main__':
    if list_search(9999999) > set_search(9999999): # means that list taking more time
        print('set search is best')
    else:
        print('list search is best')
