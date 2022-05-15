"""
Day 25: All the Same
Create a function called all_the_same that takes one argument, a string, a list, or 
a tuple and checks if all the elements are the same. If the elements are the same, 
the function should return True. If not, it should return False. For example, 
[‘Mary’, ‘Mary’, ‘Mary’] should return True.
"""


def all_the_same(param):
    for i in param:
        if param[0] == i:
            continue
        else:
            return False
    return True


# test 
print(all_the_same(['Mary', 'Mary']))
print(all_the_same(['Mary', 'Mary', 'santa']))
