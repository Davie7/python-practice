"""
The simplest impossible math problem".You start with any positive interger.
if the intrger is even,you divide it by 2.If it is odd,you multiply it by 3 and
add 1 to the result.You keep doing this until you get 1.Interestingly enough,
no matter what positive interger you start with,it always decomposes to 1
eventually.The Collatz Sequence doesn't apply for 0.
"""
def collatz(number):
        while number != 1:
            if number <= 0:
                print("This isn't a positive interger.It doesn't count")
                break

            elif number % 2 == 0:
                number = number // 2
                print(number)

            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)

while True:
    try:
        number = int(input("Please enter a positive integer for the Collatz \
Sequence to work its magic: "))
        collatz(number)
        break
    except (ValueError, NameError , TypeError):
        print('Please enter positive integers only')

        
    

    
