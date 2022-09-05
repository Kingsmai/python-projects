# This is a guess a number game.
import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)
print('DEBUG: Secret number is ' + str(secretNumber))

# Ask the player to guess 6 times.
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job %s! You guessed my number in %d guesses.' % (name, guessTaken))
else:
    print('Nope, the number I was thinking was ' + str(secretNumber))