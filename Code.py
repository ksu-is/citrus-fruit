Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class user(object):

    #First we define the variables that we would like to use

    def __init__(self, age, weight, height, chromosomes, activity, diet, effect):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity = activity_level
        self.diet = diet
        self.effect = effect

        if gender == 1:
            self.biology = male_biology
        elif chromosomes == 2:
            self.biology = female_biology
        else:
            raise Exception('Invalid gender')

gender = input('What is the gender?: ')
print(self.biology)
