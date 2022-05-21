"""
Day 43: Student Marks
Write a function called student_marks that records marks achieved by students in a 
test. The function should ask the user to input the name of the student and then ask 
the user to input the marks achieved by the student. The information should be stored
in a dictionary. The name is the key and the marks are the value. When the user 
enters done, the function should return a dictionary of names and values entered.
"""


def student_marks():
    student_marks = dict()
    # ask for student name
    while (std_name := input('Enter Student name: ')) != 'done':
        # ask for student score
        try:
            std_score = float(input("Enter score Obtained by student: "))
            if std_score < 0 or std_score > 100:
                raise ValueError
        except ValueError:
            print('please provide the value between 0-100')
        student_marks[std_name] = std_score
    return student_marks


print(student_marks())
