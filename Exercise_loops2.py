print("This program asks the user for 8 names of people and stores them in a list.When all the names have been given,pick a random one and print it.")

import random

for x in range(0,8):
    person = input("Type the name of a person: ")
    people.append(person)


index = random.randint(0,7)

ramdom_person = people[index]

print("Picking a random person: ",random_person)
