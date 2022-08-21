import random

PICO = 'Pico'
FERM = 'Fermi'
BAGE = 'Bagels'

NUM_DIGITS = 3
MAX_GUESSES = 10

print('Bagels, a deductive logic game.')
print(f'''I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.
Here are some clues:
When I say:\tThat means:
    {PICO.ljust(7)}\tOne digit is correct but in the wrong position.
    {FERM.ljust(7)}\tOne digit is correct but in the right position.
    {BAGE.ljust(7)}\tNo digit is correct.
    
For example, if the secret number was 248 and your guess was 843,
the clues would be Fermi Pico.''')

def getSecretNum():
  '''Returns a string made up of NUM_DIGITS unique random digits.'''
  numbers = list('0123456789')
  random.shuffle(numbers)

  secret_num = ''
  for i in range(NUM_DIGITS):
    secret_num += numbers[i]
  return secret_num

def getClues(guess = str, secret_num = str) -> str:
  """Returns the string with the PICO, FERM, BAGE clues for a guess
  and secret number pair"""
  if guess == secret_num:
    return 'You got it!'

  clues = []

  for i in range(len(guess)):
    if guess[i] == secret_num[i]:
      clues.append(FERM)
    elif guess[i] in secret_num:
      clues.append(PICO)
  
  if len(clues) == 0:
    return BAGE
  
  # Sort the clues into alphabetical order so their original order
  # doesn't give any information away
  clues.sort()
  return ' '.join(clues)

def main():
  # Program main loop
  while True:

    secret_number = getSecretNum()

    print(f'''I have thought up a number.
    You have {MAX_GUESSES} guesses to get it''')

    num_guesses = 1

    while num_guesses <= MAX_GUESSES:
      guess = ''
      # Keep looping until they enter a valid guess
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print(f'Guess #{num_guesses}:')
        guess = input('> ')

        clue = getClues(guess, secret_number)
        print(clue)

        num_guesses += 1

      if guess == secret_number:
        # Break the loop because the player win
        break

      if num_guesses > MAX_GUESSES:
        print('You ran out the guesses.')
        print(f'The correct answer was {secret_number}.')

    print('Do you want to play again? (Y/n)')
    if not input('> ').lower().startswith('y'):
      break
  print('Thanks for playing.')

if __name__ == '__main__':
  main()