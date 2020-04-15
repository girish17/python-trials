import random
import unicodedata

choice = 'hit'
cards = {'A of Hearts':11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9, '10 of Hearts' : 10, 'J of Hearts' : 10, 'Q of Hearts' : 10, 'K of Hearts' : 10,
         'A of Spades':11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9, '10 of Spades' : 10, 'J of Spades' : 10, 'Q of Spades' : 10, 'K of Spades' : 10,
         'A of Diamonds':11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9, '10 of Diamonds' : 10, 'J of Diamonds' : 10, 'Q of Diamonds' : 10, 'K of Diamonds' : 10,
         'A of Clubs':11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9, '10 of Clubs' : 10, 'J of Clubs' : 10, 'Q of Clubs' : 10, 'K of Clubs' : 10}
playingCardUnicode = {'A of Hearts':'\U0001F0B1', '2 of Hearts': '\U0001F0B2', '3 of Hearts': '\U0001F0B3', '4 of Hearts': '\U0001F0B4', '5 of Hearts': '\U0001F0B5', '6 of Hearts': '\U0001F0B6', '7 of Hearts' : '\U0001F0B7', '8 of Hearts' : '\U0001F0B8', '9 of Hearts' : '\U0001F0B9', '10 of Hearts' : '\U0001F0BA', 'J of Hearts' : '\U0001F0BB', 'Q of Hearts' : '\U0001F0BD', 'K of Hearts' : '\U0001F0BE',
         'A of Spades':'\U0001F0A1', '2 of Spades': '\U0001F0A2', '3 of Spades': '\U0001F0A3', '4 of Spades': '\U0001F0A4', '5 of Spades': '\U0001F0A5', '6 of Spades': '\U0001F0A6', '7 of Spades' : '\U0001F0A7', '8 of Spades' : '\U0001F0A8', '9 of Spades' : '\U0001F0A9', '10 of Spades' : '\U0001F0AA', 'J of Spades' : '\U0001F0AB', 'Q of Spades' : '\U0001F0AD', 'K of Spades' : '\U0001F0AE',
         'A of Diamonds': '\U0001F0C1', '2 of Diamonds': '\U0001F0C2', '3 of Diamonds': '\U0001F0C3', '4 of Diamonds': '\U0001F0C4', '5 of Diamonds': '\U0001F0C5', '6 of Diamonds': '\U0001F0C6', '7 of Diamonds' : '\U0001F0C7', '8 of Diamonds' : '\U0001F0C8', '9 of Diamonds' : '\U0001F0C9', '10 of Diamonds' : '\U0001F0CA', 'J of Diamonds' : '\U0001F0CB', 'Q of Diamonds' : '\U0001F0CD', 'K of Diamonds' : '\U0001F0CE',
         'A of Clubs': '\U0001F0D1', '2 of Clubs': '\U0001F0D2', '3 of Clubs': '\U0001F0D3', '4 of Clubs': '\U0001F0D4', '5 of Clubs': '\U0001F0D5', '6 of Clubs': '\U0001F0D6', '7 of Clubs' : '\U0001F0D7', '8 of Clubs' : '\U0001F0D8', '9 of Clubs' : '\U0001F0D9', '10 of Clubs' : '\U0001F0DA', 'J of Clubs' : '\U0001F0DB', 'Q of Clubs' : '\U0001F0DD', 'K of Clubs' : '\U0001F0DE'}
count = 0
firstHandCheck = True
firstCard = random.choice(list(cards.keys()))
count += cards[firstCard]
#since the card is dealt, we shall remove it from the deck
cards.pop(firstCard)
secondCard = random.choice(list(cards.keys()))
count += cards[secondCard]
#since the card is dealt, we shall remove it from the deck
cards.pop(secondCard)

if count == 22:
    #simply because two A's means 12
    count = 12

#this is to print the unicode symbol for playing cards    
symbolOfFirstCard = unicodedata.name(playingCardUnicode[firstCard])
symbolOfSecondCard = unicodedata.name(playingCardUnicode[secondCard])
print(unicodedata.lookup(symbolOfFirstCard))
print(unicodedata.lookup(symbolOfSecondCard))

if count == 21:
    print("BlackJack! You won.")
else:
    print("Your score is: ", count)
    choice = input('Hit or stay (type hit or stay): ')
    while choice in ['hit', 'yes', 'y', 'h']:
        newCard = random.choice(list(cards.keys()))
        #this is to print the unicode symbol for playing cards
        symbolOfNewCard = unicodedata.name(playingCardUnicode[newCard])
        print("Your new card is: ", unicodedata.lookup(symbolOfNewCard))
        if newCard[0] == 'A':
            if count < 11:
                count += 11
            else:
                count += 1
        elif (firstCard[0] == 'A' or secondCard[0] == 'A') and firstHandCheck == True:
            if count < 11:
                count += cards[newCard]
            else:
                count += cards[newCard]
                if count > 21:
                    count = count-10
            firstHandCheck = False
        else:
            count += cards[newCard]

        #since the card is dealt, we shall remove it from the deck
        cards.pop(newCard)    

        if count > 21:
            print("Bust!")
            break
        elif count == 21:
            print("BlackJack! You won.")
            break
        else:
            print("Your score is: ", count)
            choice = input('Hit or stay (type hit or stay): ')
