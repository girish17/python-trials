import random

choice = 'y'

while choice in ['y', 'yes', 'YES']:
    rules = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
    player = input('enter rock, paper, or scissors.: ')
    print(player)

    cpu = random.choice(['rock', 'paper', 'scissors'])
    print(cpu)

    if player == cpu:
        print("it's a tie! no one wins")
    elif rules[player] == cpu:
        print('Player wins!')
    else:
        print('CPU wins!')

    choice = input('do you want to play again? (y/n): ')

