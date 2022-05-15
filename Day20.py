"""
Day 20: Capitalize First Letter
Write a function called capitalize. This function takes a string as an argument and 
capitalizes the first letter of each word. For example, ‘i like learning’ becomes
‘I Like Learning’.
"""


def capitalize(sentence: str) -> str:
    return ' '.join([x.capitalize() for x in sentence.split()])


def capitalized(sentence: str) -> str:
    capitalized_str = ''
    for i in range(len(sentence)):
        if i == 0:
            capitalized_str += sentence[i].upper()
        elif sentence[i-1] in [' ', '.', '?', '!', '', ',']:  # after sentence ending capitals
            capitalized_str += sentence[i].upper()
        else:
            capitalized_str += sentence[i].lower()
    return capitalized_str


print(capitalize('i like learning'))
print(capitalize('i like learning.Do you like learning? Yeah, not that much'))
print(capitalized('i like learning'))
print(capitalized('i like learning.Do you like learning?Yeah,not that much'))
