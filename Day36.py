"""
Day 36: Count String
Write a function called count that takes one argument a string, and returns a 
dictionary of how many times each element appears in the string. For example ‘hello’ 
should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}.
"""


def count(word: str):
    count_dict = dict()
    for w in word:
        try:
            count_dict[w] += 1
        except KeyError:
            count_dict[w] = 1
    return count_dict


print(count('hello'))
