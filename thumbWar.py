import random

choice = 'y'
player_score = 0
comp_score = 0
while choice in ['y', 'Y', 'Yes']:
    p = random.choice([1,2,3,4,5,6,7,8,9,10])
    print(p, '- player')
    c = random.choice([1,2,3,4,5,6,7,8,9,10])
    print(c, '- computer')
    if p > c:
        print ("player wins! ")
        player_score += 1
    elif p < c:
        print("computer wins!")
        comp_score += 1
    else:
        print ("It's a tie! no one gets a point.")
    print("Your score so far is: ", player_score)
    print("Computer's score so far is: ", comp_score)
    choice = input("Would you like to play again('y' or 'n')?: ")

print("Your score is: ", player_score)
print("Computer score is: ", comp_score)
