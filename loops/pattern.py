no_of_lines = input('How many lines would you like to print? ')
pattern = ''
odd = 1
while no_of_lines > 0:
    spaces = no_of_lines - 1
    '''print spaces'''
    while spaces > 0:
        pattern = pattern + ' '
        spaces = spaces - 1
    '''print dollars'''
    dollars = odd
    while dollars > 0:
        pattern = pattern + '$'
        dollars = dollars - 1
    pattern = pattern + '\n'
    odd = odd + 2
    no_of_lines = no_of_lines - 1

print pattern


