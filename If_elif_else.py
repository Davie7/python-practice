data_valid = False

while data_valid == False:
    grade1 = float(input("Type the first grade of the first test:"))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float(input("Type the second grade of the second test:"))
    if grade1 < 0 or grade1 > 10: 
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = int(input("Type the total number of classes:"))
    if total_classes <= 0: 
        print("The number of classes can't be zero or less")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = int(input("Type the number of absences:"))
    if absences < 0 or absences > total_classes: 
        print("The number of classes can't be less than zero or greater than the number of total classes")
        continue
    else:
        data_valid = True



avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences) / total_classes

print("Average grade:", round(avg_grade,2))
print("Attendance rate:", str(round((attendance * 100),2)) + "%")
      
if(avg_grade >=6 ) :
    if(attendance >=0.8):
        print("The student was approved.")
    else:
        print("The student has failed due to attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average lower than 6.0.")
else:
    print("The student has failed due to an average garde lower than 6.0 and an attendance rate lower than 80%.")
    
    
