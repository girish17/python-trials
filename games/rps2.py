import random

choice = 'y'

while choice in ['y', 'Y', 'yes', 'YES']:
    rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    player = input('enter rock(r), paper(p), or scissors(s).: ')
    if player.startswith('r') or player.startswith('R'):
        player = 'rock'
    elif player.startswith('p') or player.startswith('P'):
        player = 'paper'
    elif player.startswith('s') or player.startswith('S'):
        player = 'scissors'
    else:
        print("Invalid input!")
        break
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

