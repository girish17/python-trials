import random

choice = 'hit'
cards = {'A':11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10}
count = 0
firstHandCheck = True
firstCard = random.choice(list(cards.keys()))
secondCard = random.choice(list(cards.keys()))
count = cards[firstCard] + cards[secondCard]
print(firstCard)
print(secondCard)
if count == 21:
    print("BlackJack! You won.")
else:
    print("Your score is: ", count)
    choice = input('Hit or stay (type hit or stay): ')
    while choice in ['hit', 'yes', 'y', 'h']:
        newCard = random.choice(list(cards.keys()))
        print("Your new card is: ", newCard)
        if newCard == 'A':
            if count < 11:
                count += 11
            else:
                count += 1
        elif (firstCard == 'A' or secondCard == 'A') and firstHandCheck == True:
            if count < 11:
                count += cards[newCard]
            else:
                count = count-10+cards[newCard]
                firstHandCheck = False
        else:
            count += cards[newCard]
            
        if count > 21:
            print("Bust!")
            break
        elif count == 21:
            print("BlackJack! You won.")
            break
        else:
            print("Your score is: ", count)
            choice = input('Hit or stay (type hit or stay): ')
