"""
Day 4: Only Floats
Write a function called only_floats, which takes two parameters a and b, and returns 
2 if both arguments are floats, returns 1 if only one argument is a float, and returns 
0 if neither argument is a float. If you pass (12.1, 23) as an argument, your function
should return a 1.
"""


def only_floats(a, b) -> int:
    return 2 if type(a) == type(b) == float else 1 if (type(a) == float or type(b) == float) else 0


# test
print(only_floats(12.1, 23))
print(only_floats(1, 1))
print(only_floats(111.0, 1.0))
