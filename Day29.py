"""
Day 29: Middle Figure
Write a function called middle_figure that takes two parameters a, and b. The two 
parameters are strings. The function joins the two strings and finds the middle 
element. If the combined string has a middle element, the function should return the 
element, otherwise, return ‘no middle figure’. Use ‘ make love’ as an argument for a 
and ‘not wars’ as an argument for b. Your function should return ‘e’ as the middle 
element. Whitespaces should be removed.
"""


def middle_figure(a, b):
    all_string = "".join(a.split()+b.split())
    if len(all_string) > 3:
        return all_string[len(all_string)//2]
    return 'no middle figure'


print(middle_figure('make love', 'not wars'))
print(middle_figure('a', 'b'))
