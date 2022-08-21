import datetime
import random


def getBirthdays(number_of_birthdays) -> list[datetime.date]:
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant in our simulation, as long as all birthdays have same year
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year
        random_numbers_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_numbers_of_days
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of the birthday that occurs more than one in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # Set is unique, all birthday are unique

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA


def main():
    print("""Birthday Paradox

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")

    # Set up a tuple of month names in order
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    while True:  # Keep asking until the user enters a valid amount.
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            num_birthday = int(response)
            break  # User has entered a valid amount.
    print()

    # Generate and display the birthdays
    print(f"Here are {num_birthday} birthdays:")
    birthdays = getBirthdays(num_birthday)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # display a comma for each birthday after the first birthday.
            print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = f'{month_name} {birthday.day}'
        print(date_text, end='')
    print()
    print()

    match = getMatch(birthdays)

    # Display the result
    print('In this simulation, ', end='')
    if match != None:
        month_name = MONTHS[match.month - 1]
        date_text = f'{month_name} {match.day}'
        print(f'multiple people have birthday on {date_text}')
    else:
        print('there are no matching birthdays.')
    print()

    # Run the simulation 100000 times
    print(f'Generating {num_birthday} random birthdays 100,000 times...')
    input('Press ENTER to begin...')

    print('Let\'s run another 100,000 simulation.')

    sim_match = 0

    for i in range(100000):
        # Report on the progress every 10,000 simulations:
        if i % 10000 == 0:
            print(f'{i} Simulation run...')
        birthdays = getBirthdays(num_birthday)
        if getMatch(birthdays) != None:
            sim_match += 1
    print('100,000 simulations run...')

    # Display simulation results:
    probability = round(sim_match / 100000 * 100, 2)
    print(f'''
    Out of 100,000 simulations of {num_birthday} people, there was a
    matching birthday in that group {sim_match} times. This means
    that {num_birthday} people have a {probability} % chance of
    having a matching birthday in their group.
    That\'s probably more than you would think!
    ''')


if __name__ == '__main__':
    main()
