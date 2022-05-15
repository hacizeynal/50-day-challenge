"""
Write a function called index_position. This function takes a string as a parameter 
and returns the positions or indexes of all lower letters in the string. For example 
‘LovE’ should return [1,2].
"""
def index_position(parameter:str)->list:
   return [i for i, j in enumerate(list(parameter)) if j.islower()]
    

print(index_position('LovE'))
print(index_position('rAn'))
print(index_position('wooD'))