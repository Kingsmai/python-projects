import random

# Set up the constants
SPADES = chr(9824)
HEARTS = chr(9829)
CLUBS = chr(9827)
DIAMONDS = chr(9830)
BACKSIDE = 'backside'

STARTING_MONEY = 5000

def betMoney(max_bet):
  
  pass

def main():
  print('''
  Rules:
    - Try to get as close to 21 without going over.
    - Kings, Queens, and Jacks are worth 10 points.
    - Aces are worth 1 or 11 points.
    - Cards 2 through 10 are worth their face value.
    - (H)it to take another card.
    - (S)tand to stop taking cards.
    - On your first play, you can (D)ouble down to increase your bet
    - but must hit exactly one more time before standing.
    - In case of a tie, the bet is returned to the player.
    - The dealer stops hitting at 17.
  ''')

  money = STARTING_MONEY

  while True:
    # Check player have money
    if money <= 0:
      print('You\'re broke!')
      print('Great thing you weren\'t playing with real money.')
      print('Thanks for playing!')
      quit()

    # Let the player enter their bet this round:
    print(f'Money: {money}')
