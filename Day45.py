"""
Day 45: Words and Special Characters
Write a function called analyse_string that returns the number of special characters 
(#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words, and, total characters (all letters and 
special characters minus whitespaces) in a string. Return everything in a dictionary 
format:
{“special character”: “number”, “words”: “number”, “total characters”: “number”}
Use the string below as an argument:
“Python has a string format operator %. This functions analogously to printf format 
strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".
"""


def update_dictionary(source_dict: dict, key_to_update: str):
    try:
        source_dict[key_to_update] += 1
    except KeyError:
        source_dict[key_to_update] = 1


def analyse_string(paragraph: str):
    result = dict()
    for i in paragraph:
        if i in '#$%&\'()*+,-."/:;<=>?@[\]^_`{|}~':
            update_dictionary(result, 'Special Character')
    result['words'] = paragraph.count(" ")+1
    result['total Characters'] = len(''.join(paragraph))
    return result


string_paragraph = """Python has a string format operator %. This functions analogously
 to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to 
 "spam=blah eggs=2"""

print(analyse_string(string_paragraph))
