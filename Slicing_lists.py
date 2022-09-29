players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

original = ['pizza', 'falafel', 'carrot cake']
copy = original[:]
print(copy)

original.append('steak')
copy.append('fries')
print(original)
print(copy)
