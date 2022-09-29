#Start with users that need to be verified
#and an empty list to hold confirmed users

unconfirmed_users = ['bandit', 'thomas', 'shelby']
confirmed_users = []

#verify each user until there are no more confirmed users
#moved each confirmed user into the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users
print(f"\nThe following are confirmed users:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
