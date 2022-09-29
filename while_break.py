prompt = "Which city have you visited?"
prompt += "\nEnter quit to end the program: "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break

    else:
        print(f"I would love to visit {city.title()}")
