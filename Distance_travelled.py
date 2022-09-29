while True:
    print('Type in the speed of the automobile:')
    speed = input()
    if speed.isdecimal():
        break
    print('Please type in a positive integer.')


while True:
    print('Type in the time taken for the journey:')
    time = input()
    if time.isdecimal():
        break
    print('Please type in a positive integer.')

print("In " + str(time) + " hours, the car will travel " +str(int(speed) *int(time))+"km")
