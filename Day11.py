"""
Day 11: Are They Equal?
Write a function called equal_strings. The function takes two strings as arguments 
and compares them. If the strings are equal (if they have the same characters and 
have equal length), it should return True, if they are not, it should return False. 
For example, ‘love’ and ‘evol’ should return True.
"""


def equal_strings(str1:str, str2:str)->bool:
    return sorted(str1.lower()) == sorted(str2.lower())


# test
print(equal_strings('love', 'evol'))
print(equal_strings('work', 'york'))
print(equal_strings('nep', 'pen'))
print(equal_strings('ten', 'NET'))
