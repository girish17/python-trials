n = input("how many lines should the pyramid have?")
pattern = ''

odd = 1

if n < 1:
    print"enter a bigger number"
elif n > 150:
    print"enter a smaller number"
else:

    while n > 0:
        spaces = n - 1
        '''print spaces'''
        while spaces > 0:
            pattern = pattern + ' '
            spaces = spaces - 1
        '''print asterisks'''   
        ast = odd   
        while ast > 0:  
            pattern = pattern + '*'
            ast = ast - 1
        pattern = pattern + '\n'
        odd = odd + 2
        n = n - 1

    print pattern






