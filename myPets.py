myPets = ['Zopie','Pooka','Fat-Tail']
for trials in range(len(myPets)):
    print('Enter a pet name: ')
    name = input()
    if name not in myPets:
        print('I do not have a pet named' + ' ' + name)
    else:
        print(name + ' ' + 'is my pet.')
