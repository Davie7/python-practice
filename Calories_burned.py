caloriesBurnedPerMinute = 4.2

for numberOfMinutes in range(10,31,5):
    numberOfCaloriesBurned = ( numberOfMinutes / 1) * caloriesBurnedPerMinute
    print("You will burn " + str(numberOfCaloriesBurned)+ " calories in " + 
          str(numberOfMinutes) + " minutes")    
