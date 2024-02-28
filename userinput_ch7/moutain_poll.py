responses = {}
polling_activity = True

while polling_activity:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_activity = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like tko climb {response}.")