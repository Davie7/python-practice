print("This program calculates the BMI(Body Mass Index) of a person.")

weight = float(input("Type your weight in kilograms: "))
height = float(input("Type your height in meters: "))

bmi = weight/ (height*height)

print("Your BMI is:",round(bmi,2))

if (bmi <= 18.5):
    classification = "Underweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal weight"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "Overweight"
else:
    classification = "Obesity"

print("The classification of your BMI is:",classification)
