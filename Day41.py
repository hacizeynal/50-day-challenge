"""
Day 41: Only Words with Vowels
Create a function called words_with_vowels, this function takes a string of words and
 returns a list of only words that have vowels in them. For example 
 ‘ You have no rhythm’ should return [‘You’,’have’, ‘no’].
Extra Challenge: Class of Cars
b. Create three classes of three car brands – Ford, BMW, and Tesla. The attributes of
 the car's objects will be, model, color, year, transmission, and whether the car is 
 electric or not (Boolean value.) Consider using inheritance in your answer.
You will create one object for each car brand:
bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False 
tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True ford1 
: model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False
You will create a class method, called print_cars that will be able to print out 
objects of the class. For example, if you call the method on the ford1 object of the 
Ford class, your function should be able to print out
car info in this exact format: car_model = focus
Color = White
Year = 2020
Transmission = Auto Electric = False
"""


def words_with_vowels(words: str) -> list:
    # words_with_vowel = [word for word in words.split() for x in word if x in 'aeiou' break]
    words_with_vowel = list()
    for word in words.split():
        for w in word:
            if w.lower() in 'aeiou':
                words_with_vowel.append(word)
                break
    return words_with_vowel


print(words_with_vowels('You have no rhythm'))


class Car:
    def __init__(self, model: str, Color: str, Year: str, Transmission: str, Electric: bool):
        self._model: str = model
        self._Color: str = Color
        self._Year: str = Year
        self._Transmission: str = Transmission
        self._Electric: str = Electric

    def print_cars(self):
        return f'\ncar_model = {self._model}\n'\
            f'color = {self._Color}\n'\
            f'year = {self._Year}\n'\
            f'Transmissoin = {self._Transmission}\n'\
            f'Electric  = {self._Electric}'


class BMW(Car):
    def __init__(self, model: str, Color: str, Year: str, Transmission: str, Electric: bool):
        super().__init__(model, Color, Year, Transmission, Electric)


class Tesla(Car):
    def __init__(self, model: str, Color: str, Year: str, Transmission: str, Electric: bool):
        super().__init__(model, Color, Year, Transmission, Electric)


class Ford(Car):
    def __init__(self, model: str, Color: str, Year: str, Transmission: str, Electric: bool):
        super().__init__(model, Color, Year, Transmission, Electric)


if __name__ == '__main__':
    bmw1 = BMW('x6', 'Red', '2016', 'Auto', False)
    print(bmw1.print_cars())

    tesla = Tesla('S', 'beige', '2017', 'Auto', True)
    print(tesla.print_cars())

    ford1 = Ford('Focus', 'white', '2020', 'Auto', False)
    print(ford1.print_cars())
