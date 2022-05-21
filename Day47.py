'''
Day 47: Save a JSON
Write a function called save_json. This function takes a dictionary below as an 
argument and saves it on a file in JSON format.
Write another function called read_json that opens the file that you
just saved and reads its content.
names = {'name': 'Carol','sex': 'female','age': 55}
'''

import json


def save_json(data_to_save: dict):
    with open('data.json', 'w')as file:
        json.dump(data_to_save, fp=file, indent=2)


names = {'name': 'Carol', 'sex': 'female', 'age': 55}
save_json(names)


def read_json():
    with open('data.json') as file:
        data = json.load(file)
        print(data)

read_json()