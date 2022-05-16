"""
Write a function called check_pangram that takes a string and checks if it is a 
pangram. A pangram is a sentence that contains all the letters of the alphabet. 
If it is a pangram, the function should return True, otherwise, return False. The 
following sentence is a pangram so it should return True:
'the quick brown fox jumps over a lazy dog'
"""


def check_pangram(sentence: str) -> bool:
    a_to_z = 'abcdefghijklmnopqrstuvwxyz'
    return a_to_z == ''.join(sorted(set(''.join(sentence.lower().split()))))


print(check_pangram('the quick brown fox jumps over a lazy dog'))
print(check_pangram('This is my test string'))
