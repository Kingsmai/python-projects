import random

SUIT = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck


def getCard(deckListIn) -> dict:
    thisCard = deckListIn.pop()  # pop one off the top of the deck and return
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck


def shuffle(deckListIn: list) -> list:
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code


def main():
    print('Welcome to Higher or Lower.')
    print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
    print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
    print('You have 50 points to start.')
    print()

    startingDeckList = []

    for suit in SUIT:
        for thisValue, rank in enumerate(RANK):
            cardDict = {
                'rank': rank,
                'suit': suit,
                'value': thisValue + 1
            }
            startingDeckList.append(cardDict)

    score = 50

    while True:  # play multiple games
        print()
        gameDeckList = shuffle(startingDeckList)
        currentCardDict = getCard(gameDeckList)
        currentCardRank = currentCardDict['rank']
        currentCardValue = currentCardDict['value']
        currentCardSuit = currentCardDict['suit']
        print('Starting card is: ', currentCardRank, ' of ', currentCardSuit)
        print()

        for cardNumber in range(0, NCARDS):  # play one game of this may cards
            answer = ''
            nextCardDict = getCard(gameDeckList)
            nextCardRank = nextCardDict['rank']
            nextCardValue = nextCardDict['value']
            nextCardSuit = nextCardDict['suit']
            while answer != 'h' and answer != 'l':
                print('Will the next card be (h)igher or (l)ower than the ', currentCardRank, ' of ', currentCardSuit)
                answer = input('> ').casefold()  # force lowercase

                if answer == 'h' or answer == 'l':
                    print('Next card is: ', nextCardRank, ' of ', nextCardSuit)
    
                if answer == 'h':
                    if nextCardValue > currentCardValue:
                        print('You got it right, it was higher')
                        score += 20
                    else:
                        print('Sorry, it was not higher')
                        score -= 15
                elif answer == 'l':
                    if nextCardValue < currentCardValue:
                        print('You got it right, it was lower')
                        score += 20
                    else:
                        print('Sorry, it was not lower')
                        score -= 15
                else:
                    print('Incorrect input, please try again')
                    print()

            print('Your score is: ', score)
            print()
            currentCardRank = nextCardRank
            currentCardSuit = nextCardSuit
            currentCardValue = nextCardValue

        print('To play again, press ENTER, or "q" to quit')
        goAgain = input('> ').casefold()

        if goAgain == 'q':
            break

    print('Ok, bye.')


if __name__ == '__main__':
    main()
