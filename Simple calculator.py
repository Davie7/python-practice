while True:
    print("Options")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input=input(": ")

    if user_input=="quit":
        break
    elif user_input=="+":
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        result=(num1 + num2)
        print(f'The answer is {result}')
    elif user_input=="-":
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        result=(num1 - num2)
        print(f'The answer is {result}')
    elif user_input=="*":
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        result=(num1 * num2)
        print(f'The answer is {result}')
    elif user_input=="/":
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        result=(num1 / num2)
        print(f'The answer is {result}')
