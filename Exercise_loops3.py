import random

print("This program is a guess game with the name of colors.At each round pick a random color from a list and let the user try to guess it.When he does it,ask if he wants to play again.Keep playing until the user types 'no'")

colors = ["white" , "black" , "red" , "green" , "blue" , "yellow" ,"purple" , "grey"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color,can you guess it: ")


    while True:
        if (color == guess.lower()):
            break
        else:
            guess = input("Nope.Try again: ")

    print("You guessed it! I was thinking about", color)

    play_again = input("Press 'enter' to play again or Type 'no' to quit.")

    if play_again.lower() == 'no':
        break
print("It was fun, thanks for playing! ")

