"""
Write a function called translate that takes the following words and translates them 
into pig Latin.
a = 'i love python'
Here are the rules:
1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the end.
For example ‘eat’ will become ‘eatyay’
2. If a word starts with anything other than a vowel, move the
first letter to the end and add ‘ay’ to the end. For example
‘day’ will become ‘ayday’.
Your code should return:
iyay ovelay ythonpay
"""


def translate(sentence:str)->str:
    words_to_return = []
    for word in sentence.split():
        if word[0].lower() in ['a','e','i','o','u']:
            words_to_return.append(word+'yay')
        else:
            words_to_return.append(word[1:]+word[0]+'ay')
    return ' '.join(words_to_return)


print(translate('i love python'))
