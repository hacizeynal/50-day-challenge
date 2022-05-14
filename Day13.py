"""
Day 13: Pay Your Tax
Write a function called your_vat. The function takes no parameter. The function asks 
the user to input the price of an item and VAT (vat should be a percentage). The 
function should return the price of the item plus VAT. If the price is 220 and, VAT 
is 15% your code should return a vat inclusive price of 253. Make sure that your 
code can handle ValueError. Ensure the code runs until valid numbers are entered. 
(hint: Your code should include a while loop).
"""


def is_valid_user_input(user_input) -> bool:
    try:
        user_input = float(user_input)
        return True
    except ValueError:
        return False


def your_vat():
    price = input('Enter valid price again: ')
    VAT = input('Enter valid VAT % again: ')
    
    while True:
        if is_valid_user_input(price) and is_valid_user_input(VAT):
            break
        elif not is_valid_user_input(VAT):
            VAT = input("Plese Enter valid value for VAT: ")
        elif not is_valid_user_input(price):
            price = input('Please Enter valid value for price: ')
       
    return f'{float(price) * (1+(float(VAT)/100)):.2f}'


print(your_vat())
