grade1 = float(input("Type the first grade of the first test:"))
grade2 = float(input("Type the second grade of the second test:"))
absences = int(input("Type the number of absences:"))
total_classes = int(input("Type the total number of classes:"))


avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences) / total_classes

print("Average grade:", round(avg_grade,2))
print("Attendance rate:", str(round((attendance * 100),2)) + "%")
      
if(avg_grade >=6 and attendance >=0.8):
    print("The student was approved.")
elif (avg_grade < 6 and attendance < 0.8):
     print("The student has failed due to an average garde lower than 6.0 and an attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average lower than 6.0.")
else:
    print("The student has failed due to an attendance lower than 80%")
   
    
    
