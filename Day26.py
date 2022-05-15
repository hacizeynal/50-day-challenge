"""
Day 26: Sort Words
Write a function called sort_words that takes a string of words as an argument, 
removes the whitespaces, and returns a list of letters sorted in alphabetical order. 
Letters will be separated by commas. All letters should appear once in the list. This
means that you sort and remove duplicates. For example ‘love life’ should return as 
['e,f,i,l,o,v'].
"""

def sort_word(words:str)->list:
    return sorted(set(''.join(words.split())))

print(sort_word('love life'))