"""
Day 44: Save Emails
Create a function called save_emails. This function takes no arguments but asks the 
user to input email, and it saves the emails in a CSV file. The user can input as many
 emails as they want. Once they hit ‘done’ the function saves the emails and closes 
 the file. Create another function called open_emails. This function opens and reads 
 the content of the CSV file. Each email must be in its line. Here is an example of 
 how the emails must be saved: jj@gmail.com
kate@yahoo.com
and not like this :
jj@gmail.comkate@yahoo.com
"""


def save_emails():
    with open('email.csv', 'w') as file:
        emails = list()
        while (email := input('enter user email: ')) != 'done':
            emails.append(email)
        file.writelines('\n'.join(emails))


def open_emails():
    with open('email.csv') as file:
        for line in file.readlines():
            print(line.strip('\n'))

save_emails()
open_emails()