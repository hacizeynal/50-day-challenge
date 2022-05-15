"""
Day 14: Flatten the List
Write a function called flat_list that takes one argument, a nested list. The function
 converts the nested list into a one-dimension list. For example [[2,4,5,6]] should 
 return [2,4,5,6].
Extra Challenge: Teacher’s Salary
b. A school has asked you to write a program that will calculate teachers' salaries. 
The program should ask the user to enter the teacher’s name, the number of periods 
taught in a month, and the rate per period. The monthly salary is calculated by 
multiplying the number of periods by the monthly rate. The current monthly rate per 
period is $20. If a teacher has more than 100 periods in a month, everything above 
100 is overtime. Overtime is $25 per period. For example, if a teacher has taught 105
periods, their monthly gross salary should be 2,125. Write a function called 
your_salary that calculates a teacher’s gross salary. The function should return the
teacher’s name, periods taught, and gross salary. Here is how you should format your
output:
Teacher: John Kelly,
Periods: 105
Gross salary:2,125
"""


from unicodedata import name


def flat_list(nested_list: list) -> list:
    return [y for x in nested_list for y in x]

def teachers_salary():
    general_rate = 20
    overtime_rate = 25

    teachers_name = input("\nEnter name of Teacher: ")
    try:
        periods = int(input("\nEnter number of period Taken: "))
    except ValueError:
        print('Please Enter a valid number of period, seeting it to 0.')
        periods = 0
    if periods > 100:
        gross_salary = ((100 * general_rate) + (periods-100) * overtime_rate)
    else:
        gross_salary = periods*general_rate
    return f'\nTeacher: {teachers_name},\nPeriods: {periods},\nGross Salary:{gross_salary:,}'

if __name__ ==  '__main__':
    # test
    print(flat_list([[2, 4, 5, 6]]))
    print(flat_list([[2, 4, 5, 6], [4, 5, 7, 8]]))
    print(flat_list([[2, 4, 5, 6], [1, 5, 9, 0], [0, 2, 9, 11]]))
    print(teachers_salary())