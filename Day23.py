"""
Day 23: Simple Calculator
Create a simple calculator. The calculator should be able to perform basic math 
operations, add, subtract, divide and multiply. The calculator should take input 
from users. The calculator should be able to handle ZeroDivisionError, NameError, and
ValueError.
"""


def get_operation_done():

    while True:
        try:
            values1 = float(input('Enter first value:'))
            values2 = float(input('Enter second value:'))
            operation = input("Enter value to for operation:\n + For add\n - For subtract\n * For multiply\n / For Divide\n . To Exit\n")
            if operation == '+':
                print(f'{values1} + {values2} = {values1+values2}')
            elif operation == '-':
                print(f'{values1} - {values2} = {values1-values2}')
            elif operation == '*':
                print(f'{values1} * {values2} = {values1*values2}')
            elif operation == '/':
                if values2 == 0:
                    raise ZeroDivisionError
                print(f'{values1} / {values2} = {values1/values2}')
            elif operation == '.':
                print('No opeation choosen Exiting...')
                break
            else:
                raise NameError
        except ZeroDivisionError:
            print("Divisor can't be Zero!!")
        except NameError:
            print("operation not found")
        except ValueError:
            print("Invalid operation/ opearnd type")


if __name__ == '__main__':
    print("****WELCOME TO CALCULATOR****")
    get_operation_done()
    print("****Thank you for Using Calulator****")
