"""
Day 30: Most Repeated Name
Write a function called repeated_name that finds the most repeated name in the following
list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
Extra Challenge: Sort by Last Name
b. You work for a local school in your area. The school has a list of names of 
students saved in a list. The school has asked you to write a program that takes a 
list of names and sorts them alphabetically. The names should be sorted by last names
. Here is a list of names:
['Beyonce Knowles, 'Alicia Keys', 'Katie Perry', 'Chris Brown',' Tom Cruise']
Your code should not just sort them alphabetically, but it should also switch the 
names (the last name must be the first). Here is how your code output should look:
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']
Write a function called sorted_names.

"""


def repeated_name(names: list) -> str:
    unique_names = sorted(set(names))
    counts_dict = dict()
    for i in unique_names:
        counts_dict[i] = names.count(i)
    return (sorted(counts_dict.items(), key=lambda v: v[1], reverse=True))[0][0]


print(repeated_name(["John", "Peter", "John", "Peter", "Jones", "Peter"]))


def sorted_names(names: list) -> list:
    last_first_name = [list(reversed(full_name.split()))for full_name in names]
    sorted_last_and_first = sorted(last_first_name, key=lambda k: k[0])
    return [' '.join(x) for x in sorted_last_and_first]

print(sorted_names(['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', ' Tom Cruise']))
