bday_survey = []

bday = input("What day of the month were you born?(1-31) or 'q' to finish: ")

while bday != "q":
    bday = input("What day of the month were you born?(1-31) or 'q' to finish: ")
    bday_survey.append(bday)

print(bday_survey)
