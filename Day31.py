"""
Day 31: Longest Word
Write a function that has one parameter and takes a list of words as an argument. 
The function returns the longest word from the list. Name the function longest_word. 
The function should return the longest word and the number of letters in that word. 
For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your function should return
[10, JavaScript] as the longest word.
"""


def longest_word(words: list) -> list:
    max_len_word = ''

    for word in words:
        if len(word) > len(max_len_word):
            max_len_word = word
    return [len(max_len_word), max_len_word]


print(longest_word(['Java', 'JavaScript', 'Python']))
