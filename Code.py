>>> class user(object):

    #First we define the variables that we would like to use

    def __init__(self, age, weight, height, gender, activity, diet, effect):
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
