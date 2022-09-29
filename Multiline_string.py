prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat's your name? "

name = input(prompt)
print(f"\nHello {name}")

age = int(input("How old are you? "))
if age < 18:
    print("Not old enough")
