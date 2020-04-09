import random

choice = 'hit'
cards = {'A of Hearts':11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9, '10 of Hearts' : 10, 'J of Hearts' : 10, 'Q of Hearts' : 10, 'K of Hearts' : 10,
         'A of Spades':11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9, '10 of Spades' : 10, 'J of Spades' : 10, 'Q of Spades' : 10, 'K of Spades' : 10,
         'A of Diamonds':11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9, '10 of Diamonds' : 10, 'J of Diamonds' : 10, 'Q of Diamonds' : 10, 'K of Diamonds' : 10,
         'A of Clubs':11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9, '10 of Clubs' : 10, 'J of Clubs' : 10, 'Q of Clubs' : 10, 'K of Clubs' : 10}
count = 0
firstHandCheck = True
firstCard = random.choice(list(cards.keys()))
secondCard = random.choice(list(cards.keys()))
count = cards[firstCard] + cards[secondCard]
if count == 22:
    #simply because two A's means 12
    count = 12
print(firstCard)
print(secondCard)

#since the card is dealt, we shall remove it from the deck
cards.pop(firstCard)
cards.pop(secondCard)

if count == 21:
    print("BlackJack! You won.")
else:
    print("Your score is: ", count)
    choice = input('Hit or stay (type hit or stay): ')
    while choice in ['hit', 'yes', 'y', 'h']:
        newCard = random.choice(list(cards.keys()))
        print("Your new card is: ", newCard)
        if newCard[0] == 'A':
            if count < 11:
                count += 11
            else:
                count += 1
        elif (firstCard[0] == 'A' or secondCard[0] == 'A') and firstHandCheck == True:
            if count < 11:
                count += cards[newCard]
            else:
                if count < 11:
                    count += 11
                else:
                    count = count-10+cards[newCard]
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
