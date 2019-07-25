# gain user input on variables for 
age = input("What is your age? ")
weight = input("What is your weight in lbs? ")
height = input("What is your height in inches? ")
gender = input ("Are you male or female? Input XY for male, or XX for female: ")
activity = input("What is your activity level? Sedentary, Light, Moderate, Active, or Extreme?: ") 
goal = input("Do you want to Gain, Lose, or Maintain weight?: ")
diet = input("Do you want the Keto diet or Standard?: ")

# the harris-benedict base metabolic rate is different for men and women
xy_biology_formula = 66.47 + (6.42 * int(weight)) + (12.7 * int(height)) - (6.755 * int(age))
xx_biology_formula = 655.1 + (4.35 * int(weight)) + (4.7 * int(height)) - (4.7 *int(age))

if gender == 'XY':
    biology = xy_biology_formula
elif gender == 'XX':
    biology = xx_biology_formula
else:
    raise Exception('Invalid chromosomes')

base_metabolic_rate = print("Your basal metabolic rate is: ", biology, "calories")
bmi = int(weight) * 703 / (int(height) * int(height))
print("Your body mass index is: ", bmi)
if activity == "Sedentary":
    print("Your maintenance calories are : ", biology * 1.2)
elif activity == "Light":
    print("Your maintenance calories are: ", biology * 1.375)
elif activity == "Moderate":
    print("Your maintenance calories are: ", biology * 1.55)
elif activity == "Active":
    print("Your maintenance calories are: ", biology * 1.725)
elif activity == "Extreme":
    print("Your maintenance calories are: ", biology * 1.9) 
else:
    pass

if goal == "Gain":
    print("Your calories to gain weight are: ", biology + 500)
elif goal == "Lose":
    print("Your calories to lose weight are: ", biology - 500)
elif goal == "Maintain":
    print("Your caloies to maintain weight are: shown above")
else:
    pass


keto_formula = ((biology / 2)/ 4, "grams of protein", (biology / 2)/ 9, "grams of fat")
standard_formula = ((biology / 3)/ 4, "grams of protein", (biology / 3)/ 9, "grams of fat",(biology / 3)/ 4, "grams of carbs")


if diet == 'Keto':
    macronutrient = keto_formula
elif diet == 'Standard':
    macronutrient = standard_formula
else:
    raise Exception('Invalid diet')
    
macronutrient_breakdown = print("Your macronutrient breakdown for the", diet, "diet is", macronutrient)
